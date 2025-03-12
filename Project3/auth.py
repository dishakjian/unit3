import re
from random import choice, randint

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.navigationbar import MDNavigationBar

from mylib import DatabaseManager
from secure_password import check_hash, hash_password

Window.size = (600, 700)

class HomeScreen(Screen):
    def go_to_restaurant_screen(self):
        self.manager.current = 'restaurant_screen'

class UserHomeScreen(Screen):
    def go_to_home_screen(self):
        self.manager.current = 'home_screen'

    def on_enter(self, *args):
        self.filter_restaurants()

    def filter_restaurants(self):
        filter_type = self.ids.filter_spinner.text
        search_query = self.ids.search_input.text.lower()

        db = DatabaseManager('project.sql')
        query = "SELECT id, name, description, rating, price, photo FROM restaurants"
        restaurants = db.search(query)
        db.close()

        print(f"Found {len(restaurants)} restaurants.")

        self.ids.restaurant_list.clear_widgets()

        if filter_type == 'Price':
            restaurants.sort(key=lambda x: x[4] if x[4] is not None else 0)
        elif filter_type == 'Rating':
            restaurants.sort(key=lambda x: x[3] if x[3] is not None else 0, reverse=True)
        elif filter_type == 'Recommended':
            db = DatabaseManager('project.sql')
            user_id = db.search("SELECT id FROM users WHERE username = ?", (LoginScreen.current_username,))[0][0]
            user_taste_profile = db.search(
                "SELECT sweet, salty, sour, bitter, umami FROM user_taste_profiles WHERE user_id = ?",
                (user_id,))
            db.close()

            if user_taste_profile:
                user_sweet, user_salty, user_sour, user_bitter, user_umami = user_taste_profile[0]

                for i, restaurant in enumerate(restaurants):
                    restaurant_id = restaurant[0]
                    restaurant_taste_profile = self.calculate_restaurant_taste_profile(restaurant_id)

                    if not restaurant_taste_profile:
                        restaurant = list(restaurant)
                        restaurant.append(0.0)
                        restaurants[i] = tuple(restaurant)
                        continue

                    recommendation_score = (
                            user_sweet * restaurant_taste_profile["sweet"] +
                            user_salty * restaurant_taste_profile["salty"] +
                            user_sour * restaurant_taste_profile["sour"] +
                            user_bitter * restaurant_taste_profile["bitter"] +
                            user_umami * restaurant_taste_profile["umami"]
                    )
                    restaurant = list(restaurant)
                    restaurant.append(recommendation_score)
                    restaurants[i] = tuple(restaurant)

                restaurants.sort(key=lambda x: x[-1], reverse=True)

        filtered_restaurants = []
        for restaurant in restaurants:
            restaurant_id, name, description, rating, price, photo, *rest = restaurant
            if not search_query or search_query in name.lower() or search_query in description.lower():
                filtered_restaurants.append(restaurant)

        for restaurant in filtered_restaurants:
            restaurant_id, name, description, rating, price, photo, *rest = restaurant
            price = price if price is not None else 3

            print(f"Creating card for: {name}")

            card = MDCard(
                orientation="vertical",
                size_hint=(1, None),
                height="180dp",
                elevation=4,
                padding=10,
                spacing=10,
                md_bg_color=(1, 1, 1, 1))

            title_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")
            title_label = Label(
                text=name,
                font_size="18sp",
                bold=True,
                size_hint_x=0.6,
                color=(0, 0, 0, 1))

            rating_box = BoxLayout(orientation='horizontal', size_hint_x=0.2, spacing=5)

            rating = rating if rating is not None else 0
            full_stars = int(rating)
            half_star = 1 if (rating - full_stars) >= 0.5 else 0
            empty_stars = 5 - full_stars - half_star

            for _ in range(full_stars):
                rating_box.add_widget(Image(source='fullstar.png', size_hint=(None, None), size=(20, 20)))

            if half_star:
                rating_box.add_widget(Image(source='star-half-icon.png', size_hint=(None, None), size=(20, 20)))

            for _ in range(empty_stars):
                rating_box.add_widget(Image(source='emptystar.png', size_hint=(None, None), size=(20, 20)))

            price_label = Label(
                text=f"¥{'¥' * price}",
                font_size="16sp",
                size_hint_x=0.2,
                color=(0, 0, 0, 1))

            title_box.add_widget(title_label)
            title_box.add_widget(rating_box)
            title_box.add_widget(price_label)

            description_label = Label(
                text=description,
                font_size="14sp",
                size_hint_y=None,
                height="60dp",
                color=(0, 0, 0, 1))

            details_button = Button(
                text="View Details",
                size_hint_y=None,
                height="40dp",
                on_release=lambda btn, rid=restaurant_id: self.view_restaurant(rid))

            card.add_widget(title_box)
            card.add_widget(description_label)
            card.add_widget(details_button)

            self.ids.restaurant_list.add_widget(card)
            print(f"Added card for: {name}")

    def view_restaurant(self, restaurant_id):
        self.manager.current = 'restaurant_detail'
        self.manager.get_screen('restaurant_detail').load_restaurant(restaurant_id)

    def calculate_restaurant_taste_profile(self, restaurant_id):
        db = DatabaseManager('project.sql')
        try:
            query = """
            SELECT d.sweet, d.salty, d.sour, d.bitter, d.umami
            FROM reviews r
            JOIN dishes d ON r.dish = d.id
            WHERE r.restaurant_id = ?
            """
            dish_taste_profiles = db.search(query, (restaurant_id,))

            if not dish_taste_profiles:
                return {
                    "sweet": 0,
                    "salty": 0,
                    "sour": 0,
                    "bitter": 0,
                    "umami": 0,
                }

            taste_profile = {"sweet": 0, "salty": 0, "sour": 0, "bitter": 0, "umami": 0}
            for dish in dish_taste_profiles:
                sweet, salty, sour, bitter, umami = dish
                taste_profile["sweet"] += sweet
                taste_profile["salty"] += salty
                taste_profile["sour"] += sour
                taste_profile["bitter"] += bitter
                taste_profile["umami"] += umami

            num_dishes = len(dish_taste_profiles)
            for key in taste_profile:
                taste_profile[key] /= num_dishes

            return taste_profile

        except Exception as e:
            print(f"Error calculating taste profile: {e}")
            return {
                "sweet": 0,
                "salty": 0,
                "sour": 0,
                "bitter": 0,
                "umami": 0,
            }
        finally:
            db.close()

class UserProfileScreen(Screen):
    def on_enter(self, *args):
        self.load_profile()

    def load_profile(self):
        db = DatabaseManager('project.sql')
        try:
            user_id = db.search("SELECT id FROM users WHERE username = ?", (LoginScreen.current_user,))[0][0]

            query = """
            SELECT 
                u.username, 
                COUNT(r.id) AS num_reviews, 
                SUM(CASE WHEN r.rating >= 4 THEN 1 ELSE 0 END) AS likes, 
                SUM(CASE WHEN r.rating < 3 THEN 1 ELSE 0 END) AS dislikes 
            FROM users u 
            LEFT JOIN reviews r ON u.id = r.user_id 
            WHERE u.username = ?
            GROUP BY u.username
            """
            profile_data = db.search(query, (LoginScreen.current_user,))
            if not profile_data:
                print("No profile data found for the user.")
                return

            profile_data = profile_data[0]
            username, num_reviews, likes, dislikes = profile_data

            taste_profile = db.search(
                "SELECT sweet, salty, sour, bitter, umami FROM user_taste_profiles WHERE user_id = ?",
                (user_id,))

            self.ids.username_label.text = f"Username: {username}"
            self.ids.num_reviews_label.text = f"Number of Reviews: {num_reviews}"

            total_feedback = likes + dislikes
            if total_feedback > 0:
                like_percentage = (likes / total_feedback) * 100
                dislike_percentage = (dislikes / total_feedback) * 100
                self.ids.like_dislike_label.text = f"Like/Dislike Ratio: {like_percentage:.1f}% 👍 / {dislike_percentage:.1f}% 👎"
            else:
                self.ids.like_dislike_label.text = "Like/Dislike Ratio: No feedback yet"

            points_query = """
            SELECT COUNT(*) 
            FROM reviews 
            WHERE user_id = ? 
            AND (likes / (likes + dislikes)) >= 0.8
            """
            points = db.search(points_query, (user_id,))[0][0]
            self.ids.points_label.text = f"Points: {points}"
            self.ids.free_meal_progress.value = points

            if taste_profile:
                sweet, salty, sour, bitter, umami = taste_profile[0]
                self.ids.sweet_label.text = f"Sweet: {sweet * 100:.1f}%"
                self.ids.salty_label.text = f"Salty: {salty * 100:.1f}%"
                self.ids.sour_label.text = f"Sour: {sour * 100:.1f}%"
                self.ids.bitter_label.text = f"Bitter: {bitter * 100:.1f}%"
                self.ids.umami_label.text = f"Umami: {umami * 100:.1f}%"
            else:
                self.ids.sweet_label.text = "Sweet: 0.0%"
                self.ids.salty_label.text = "Salty: 0.0%"
                self.ids.sour_label.text = "Sour: 0.0%"
                self.ids.bitter_label.text = "Bitter: 0.0%"
                self.ids.umami_label.text = "Umami: 0.0%"

        except Exception as e:
            print(f"Error loading profile: {e}")
        finally:
            db.close()

    def get_taste_value(self, label_text):
        try:
            return float(label_text.split(": ")[1].replace("%", ""))
        except (IndexError, ValueError):
            return 0.0

    def logout(self):
        self.manager.current = 'welcome'

class Navigation(MDNavigationBar):
    pass

Window.borderless = True

class WaitingApprovalScreen(Screen):
    pass

class RestaurantSignupScreen(Screen):
    db = DatabaseManager('project.sql')

    def on_enter(self):
        user_id = self.manager.get_screen('signup').user_id
        db = DatabaseManager('project.sql')
        self.restaurant_id = db.search("SELECT id FROM restaurants WHERE owner_id = ?", (user_id,))[0][0]
        db.close()

    def add_dishes(self):
        dishes = self.ids.dishes.text.strip().split(",")
        if not dishes:
            self.show_error("Please enter at least one dish.")
            return

        db = DatabaseManager('project.sql')
        for dish in dishes:
            dish = dish.strip()
            if dish:
                dish_query = """
                    INSERT INTO dishes (name, restaurant_id)
                    VALUES (?, ?)
                """
                db.execute(dish_query, (dish, self.restaurant_id))

        db.commit()
        db.close()
        print("Dishes added successfully!")
        self.manager.current = 'waiting_approval'

    def show_error(self, message):
        ErrorPopup(message).open()

    def submit_restaurant(self):
        restaurant_name = self.ids.restaurant_name.text.strip()
        restaurant_description = self.ids.restaurant_description.text.strip()

        if not restaurant_name or not restaurant_description:
            self.show_error("All fields are required.")
            return

        user_id = self.manager.get_screen('signup').user_id

        query = """
            INSERT INTO restaurants (name, description, owner_id, approved, sample)
            VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute(query, (
            restaurant_name,
            restaurant_description,
            user_id,
            False,
            False
        ))
        self.db.commit()

        print("Restaurant details updated.")
        self.manager.current = 'waiting_approval'

class RestaurantHomeScreen(Screen):
    def on_enter(self):
        self.load_restaurant_details()
        self.load_reviews()

    def load_restaurant_details(self):
        db = DatabaseManager('project.sql')

        username = LoginScreen.current_username
        print(f"Debug: Current username = {username}")

        if not username:
            print("Error: Username not found.")
            db.close()
            return

        user_query = "SELECT id FROM users WHERE username = ?"
        user_result = db.search(user_query, (username,))
        print(f"Debug: User query result = {user_result}")

        if not user_result:
            print("Error: User not found in the database.")
            db.close()
            return

        user_id = user_result[0][0]
        print(f"Debug: User ID = {user_id}")

        query = "SELECT id, name, description, rating FROM restaurants WHERE owner_id = ?"
        restaurant_result = db.search(query, (user_id,))
        print(f"Debug: Restaurant query result = {restaurant_result}")

        if not restaurant_result:
            print("Error: Restaurant not found for the current user.")
            db.close()
            return

        restaurant_id, name, description, rating = restaurant_result[0]
        print(f"Debug: Restaurant ID = {restaurant_id}")

        self.ids.restaurant_name.text = name
        self.ids.restaurant_description.text = description
        self.ids.restaurant_rating.text = f"Rating: {rating}"

        db.close()

    def load_reviews(self):
        db = DatabaseManager('project.sql')

        username = LoginScreen.current_username
        print(f"Debug: Current username = {username}")

        if not username:
            print("Error: Username not found.")
            db.close()
            return

        user_query = "SELECT id FROM users WHERE username = ?"
        user_result = db.search(user_query, (username,))
        print(f"Debug: User query result = {user_result}")

        if not user_result:
            print("Error: User not found in the database.")
            db.close()
            return

        user_id = user_result[0][0]
        print(f"Debug: User ID = {user_id}")

        restaurant_query = "SELECT id FROM restaurants WHERE owner_id = ?"
        restaurant_result = db.search(restaurant_query, (user_id,))
        print(f"Debug: Restaurant query result = {restaurant_result}")

        if not restaurant_result:
            print("Error: Restaurant not found for the current user.")
            db.close()
            return

        restaurant_id = restaurant_result[0][0]
        print(f"Debug: Restaurant ID = {restaurant_id}")

        query = """
        SELECT r.id, r.dish, r.rating, r.comment, r.helpful, u.username 
        FROM reviews r 
        JOIN users u ON r.user_id = u.id 
        WHERE r.restaurant_id = ?
        """
        reviews = db.search(query, (restaurant_id,))
        db.close()

        self.ids.reviews.clear_widgets()
        for review in reviews:
            review_id, dish, rating, comment, helpful, username = review
            helpful_status = "Marked as Helpful" if helpful else "Marked as Unhelpful" if helpful is not None else "Not Reviewed by Moderator"

            review_box = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=200,
                padding=10,
                spacing=10
            )

            review_box.add_widget(Label(
                text=f"User: {username}\nDish: {dish}\nRating: {rating}\nComment: {comment}\nModerator: {helpful_status}",
                color=(0, 0, 0, 1),
                halign='left',
                size_hint_y=None,
                height=180
            ))

            self.ids.reviews.add_widget(review_box)

class RestaurantInventoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_username = None
        self.producers = {}

    def submit_request(self, *args):
        producer = self.producer_spinner.text
        item = self.item_input.text
        budget = self.budget_input.text

        if producer == "Select Producer" or not item or not budget:
            self.show_error("Please fill all fields.")
            return

        try:
            budget = float(budget)
        except ValueError:
            self.show_error("Invalid budget. Please enter a number.")
            return

        username = LoginScreen.current_username
        print(f"Debug: Current username = {username}")

        if not username:
            self.show_error("Username not found.")
            return

        owner_id = self.get_owner_id(username)
        print(f"Debug: Owner ID = {owner_id}")

        if not owner_id:
            self.show_error("Owner not found.")
            return

        restaurant_id = self.get_restaurant_id(owner_id)
        print(f"Debug: Restaurant ID = {restaurant_id}")

        if not restaurant_id:
            self.show_error("Restaurant not found.")
            return

        producer_id = self.producers.get(producer)
        if not producer_id:
            self.show_error("Producer not found.")
            return

        self.send_request(restaurant_id, producer_id, item, budget)

        self.dismiss_popup()

    def get_owner_id(self, username):
        db = DatabaseManager('project.sql')
        query = "SELECT id FROM users WHERE username = ?"
        result = db.search(query, (username,))
        db.close()
        if result:
            return result[0][0]
        else:
            print(f"Error: No user found with username = {username}")
            return None

    def get_restaurant_id(self, owner_id):
        db = DatabaseManager('project.sql')
        query = "SELECT id FROM restaurants WHERE owner_id = ?"
        result = db.search(query, (owner_id,))
        db.close()
        return result[0][0] if result else None

    def send_request(self, restaurant_id, producer_id, item, budget):
        db = DatabaseManager('project.sql')
        query = """
            INSERT INTO requests (restaurant_id, producer_id, item, quantity, budget, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        quantity = 1
        status = "Pending"

        db.execute(query, (restaurant_id, producer_id, item, quantity, budget, status))
        db.commit()
        db.close()

        print(
            f"Request submitted: Restaurant ID={restaurant_id}, Producer ID={producer_id}, Item={item}, Budget={budget}")

    def on_enter(self):
        self.load_inventory()
        self.load_producers()

    def load_inventory(self):
        db = DatabaseManager('project.sql')

        username = LoginScreen.current_username
        print(f"Debug: Current username = {username}")

        if not username:
            print("Error: Username not found.")
            db.close()
            return

        user_query = "SELECT id FROM users WHERE username = ?"
        user_result = db.search(user_query, (username,))
        print(f"Debug: User query result = {user_result}")

        if not user_result:
            print("Error: User not found in the database.")
            db.close()
            return

        user_id = user_result[0][0]
        print(f"Debug: User ID = {user_id}")

        restaurant_query = "SELECT id FROM restaurants WHERE owner_id = ?"
        restaurant_result = db.search(restaurant_query, (user_id,))
        print(f"Debug: Restaurant query result = {restaurant_result}")

        if not restaurant_result:
            print("Error: Restaurant not found for the current user.")
            db.close()
            return

        restaurant_id = restaurant_result[0][0]
        print(f"Debug: Restaurant ID = {restaurant_id}")

        query = "SELECT item, quantity, max_quantity FROM inventory WHERE restaurant_id = ?"
        inventory = db.search(query, (restaurant_id,))
        print(f"Debug: Inventory query result = {inventory}")

        db.close()

        self.ids.inventory_list.clear_widgets()

        for item, quantity, max_quantity in inventory:
            is_low = quantity < 0.2 * max_quantity

            item_box = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=70,
                spacing=10,
                padding=10
            )

            item_box.add_widget(Label(
                text=f"{item.capitalize()}: {quantity} kg{' (Low!)' if is_low else ''}",
                font_size=24,
                color=(1, 0, 0, 1) if is_low else (0, 0, 0, 1)
            ))

            self.ids.inventory_list.add_widget(item_box)

        if any(quantity < 0.2 * max_quantity for _, quantity, max_quantity in inventory):
            request_button = Button(
                text="Request from Producer",
                size_hint_y=None,
                height=40,
                on_release=self.show_request_dialog
            )
            self.ids.inventory_list.add_widget(request_button)

    def load_producers(self):
        db = DatabaseManager('project.sql')
        query = "SELECT id, username FROM users WHERE role = 'Producer'"
        producers = db.search(query)
        db.close()

        self.producers = {name: id for id, name in producers}
        print(f"Debug: Producers = {self.producers}")

    def show_request_dialog(self, *args):
        content = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10,
            size_hint_y=None
        )

        content.bind(minimum_height=content.setter('height'))

        self.producer_spinner = Spinner(
            text="Select Producer",
            values=list(self.producers.keys()),
            size_hint_y=None,
            height=40
        )

        self.item_input = TextInput(
            hint_text="Item (e.g., chicken)",
            size_hint_y=None,
            height=40
        )
        self.budget_input = TextInput(
            hint_text="Budget (e.g., 1000)",
            size_hint_y=None,
            height=40
        )

        submit_button = Button(
            text="SUBMIT",
            size_hint_y=None,
            height=40
        )
        submit_button.bind(on_release=self.submit_request)

        cancel_button = Button(
            text="CANCEL",
            size_hint_y=None,
            height=40
        )
        cancel_button.bind(on_release=self.dismiss_popup)

        content.add_widget(self.producer_spinner)
        content.add_widget(self.item_input)
        content.add_widget(self.budget_input)
        content.add_widget(submit_button)
        content.add_widget(cancel_button)

        self.popup = Popup(
            title="Request Items",
            content=content,
            size_hint=(0.8, None),
            height=300,
            auto_dismiss=False
        )

        self.popup.open()

    def dismiss_popup(self, *args):
        if self.popup:
            self.popup.dismiss()

    def show_error(self, message):
        ErrorPopup(message).open()

class ProducerHomeScreen(Screen):
    def on_enter(self):
        self.load_requests()

    def load_requests(self):
        db = DatabaseManager('project.sql')
        query = """
        SELECT r.id, res.name, r.item, r.quantity, r.budget, r.status 
        FROM requests r 
        JOIN restaurants res ON r.restaurant_id = res.id 
        WHERE r.producer_id = 29 AND r.status = 'Pending'
        """
        requests = db.search(query)
        db.close()

        self.ids.requests_list.clear_widgets()

        for request in requests:
            request_id, restaurant_name, item, quantity, budget, status = request

            request_box = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=250,
                spacing=10,
                padding=10
            )

            request_box.add_widget(Label(
                text=f"Restaurant: {restaurant_name}\nItem: {item}\nQuantity: {quantity}\nBudget: ¥{budget}\nStatus: {status}",
                font_size=20,
                color=(0, 0, 0, 1),
                halign='left'
            ))

            options = self.generate_options(budget)
            for option in options:
                option_button = Button(
                    text=option["description"],
                    size_hint_y=None,
                    height=40,
                    on_release=lambda btn, req_id=request_id, opt=option: self.fulfill_request(req_id, opt)
                )
                request_box.add_widget(option_button)

            self.ids.requests_list.add_widget(request_box)

    def generate_options(self, budget):
        options = [
            {
                "description": "Economical Option (High Profit)",
                "cost": int(budget * 0.5),
                "profit": int(budget * 0.5),
                "sustainability": "Low"
            },
            {
                "description": "Sustainable Option (Low Profit)",
                "cost": int(budget * 0.8),
                "profit": int(budget * 0.2),
                "sustainability": "High"
            },
            {
                "description": "Balanced Option (Moderate Profit)",
                "cost": int(budget * 0.7),
                "profit": int(budget * 0.3),
                "sustainability": "Medium"
            }
        ]
        return [choice(options) for _ in range(2)]

    def fulfill_request(self, request_id, option):
        db = DatabaseManager('project.sql')
        try:
            db.execute("UPDATE requests SET status = 'Fulfilled' WHERE id = ?", (request_id,))
            db.commit()
            print(f"Request {request_id} fulfilled with option: {option['description']}")
        except Exception as e:
            print(f"Error fulfilling request: {e}")
        finally:
            db.close()

        self.load_requests()

class ModeratorFlaggedReviewsScreen(Screen):
    restaurant_id = None

    def on_enter(self, *args):
        self.load_flagged_reviews()

    def load_flagged_reviews(self):
        db = DatabaseManager('project.sql')
        query = """
        SELECT f.id, f.dish, f.rating, f.comment, f.reason, u.username 
        FROM flagged_reviews f 
        JOIN users u ON f.user_id = u.id
        """
        flagged_reviews = db.search(query)
        db.close()

        self.ids.flagged_reviews.clear_widgets()
        for review in flagged_reviews:
            review_id, dish, rating, comment, reason, username = review
            review_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
            review_box.add_widget(Label(
                text=f"User: {username}\nDish: {dish}\nRating: {rating}\nComment: {comment}\nReason: {reason}",
                color=(0, 0, 0, 1),
                halign='left'
            ))
            approve_btn = Button(text="Approve",
                                 size_hint_y=None,
                                 height=30,
                                 on_release=lambda btn,
                                 rid=review_id: self.approve_review(rid))
            reject_btn = Button(text="Reject", size_hint_y=None, height=30,
                                on_release=lambda btn, rid=review_id: self.reject_review(rid))
            review_box.add_widget(approve_btn)
            review_box.add_widget(reject_btn)
            self.ids.flagged_reviews.add_widget(review_box)

    def approve_review(self, review_id):
        db = DatabaseManager('project.sql')
        restaurant_id = db.search("SELECT restaurant_id FROM flagged_reviews WHERE id = ?", (review_id,))[0][0]

        flagged_review = \
        db.search("SELECT user_id, dish, rating, comment FROM flagged_reviews WHERE id = ?", (review_id,))[0]
        db.execute("INSERT INTO reviews (restaurant_id, user_id, dish, rating, comment) VALUES (?, ?, ?, ?, ?)",
                   (restaurant_id, flagged_review[0], flagged_review[1], flagged_review[2], flagged_review[3]))
        db.execute("DELETE FROM flagged_reviews WHERE id = ?", (review_id,))
        db.commit()
        db.close()
        self.load_flagged_reviews()

    def reject_review(self, review_id):
        db = DatabaseManager('project.sql')
        db.execute("DELETE FROM flagged_reviews WHERE id = ?", (review_id,))
        db.commit()
        db.close()
        self.load_flagged_reviews()

class AdminDashboardScreen(Screen):
    pass

class ErrorPopup(Popup):
    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Error'
        self.size_hint = (0.6, 0.4)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        error_label = Label(
            text=message,
            size_hint_y=None,
            height=100,
            color=[0.96, 0.98, 0.92, 1],
            font_size=20,
            halign='center',
            valign='middle',
        )
        error_label.bind(size=error_label.setter('text_size'))

        close_button = Button(
            text="Close",
            size_hint=(None, None),
            size=(100, 80),
            pos_hint={'center_x': 0.5},
            background_color=[0.26, 0.45, 0.73, 1],
            color=[1, 1, 1, 1]
        )
        close_button.bind(on_press=self.dismiss)

        layout.add_widget(error_label)
        layout.add_widget(close_button)

        self.content = layout

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.terms_accepted = False

    def toggle_terms_accepted(self, checkbox, value):
        self.terms_accepted = value

    def show_terms(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        terms_text = Label(
            text=(
                "Before you dive in, we want to let you know how we use your data:\n\n"
                "- We collect info about the dishes you try and your ratings.\n"
                "- This helps us predict dishes and restaurants you’ll love.\n"
                "- Your data is safe with us and will never be shared without consent.\n\n"
                "By clicking 'Accept', you help us improve the world of food!"
            ),
            size_hint_y=None,
            height=250,
            color=[0.96, 0.98, 0.92, 1],
        )

        close_button = Button(
            text="Close",
            size_hint_y=None,
            height=50,
            background_color=[0.76, 0.76, 0.65, 1],
            color=[0.26, 0.45, 0.73, 1]
        )
        layout.add_widget(terms_text)
        layout.add_widget(close_button)

        terms_popup = Popup(
            title="Terms and Conditions",
            content=layout,
            size_hint=(0.8, 0.4),
            background_color=[0.26, 0.45, 0.73, 1],
            separator_color=[0.76, 0.76, 0.65, 1]
        )

        close_button.bind(on_release=terms_popup.dismiss)
        terms_popup.open()

    def proceed_to_login(self):
        if self.terms_accepted:
            self.manager.current = 'login'
        else:
            ErrorPopup("Please accept the terms and conditions to proceed.").open()

    def proceed_to_signup(self):
        if self.terms_accepted:
            self.manager.current = 'signup'
        else:
            ErrorPopup("Please accept the terms and conditions to proceed.").open()

class LoginScreen(Screen):
    current_user = None
    current_username = None

    def try_login(self):
        username = self.ids.uname.text
        password = self.ids.passwd.text
        role = self.ids.role_spinner.text

        if not username or not password:
            self.show_error("Please fill in all fields.")
            return

        search_user = "SELECT id, username, email, password, role, points FROM users WHERE username = ? AND role = ?"
        db = DatabaseManager('project.sql')
        result = db.search(search_user, (username, role))

        if len(result) == 1:
            user_id, username, email, stored_hash_password, role, points = result[0]
            if check_hash(input_str=password, hash=stored_hash_password):
                LoginScreen.current_user = user_id
                LoginScreen.current_username = username

                if role == "Restaurant":
                    restaurant_query = "SELECT approved FROM restaurants WHERE owner_id = ?"
                    restaurant_result = db.search(restaurant_query, (user_id,))
                    db.close()

                    if restaurant_result:
                        approved = restaurant_result[0][0]
                        self.redirect_to_role_screen(role, approved)
                    else:
                        self.show_error("Restaurant not found.")
                        return
                else:
                    self.redirect_to_role_screen(role)
            else:
                db.close()
                self.show_error("Username or password incorrect.")
        else:
            db.close()
            self.show_error("User not found.")

    def redirect_to_role_screen(self, role, approved=None):
        role_screens = {
            'User': 'Restaurants',
            'Restaurant': 'restaurant_home_screen' if approved else 'waiting_approval',
            'Producer': 'producer_home_screen',
            'Moderator': 'moderator_flagged_reviews_screen',
            'Admin': 'admin_dashboard_screen'
        }
        self.parent.current = role_screens.get(role, 'home_screen')

    def show_error(self, message):
        ErrorPopup(message).open()

    def logout(self):
        self.current_user = None
        self.manager.current = 'login'

class ModeratorCriticismScreen(Screen):
    def on_enter(self, *args):
        self.load_criticism_reviews()

    def load_criticism_reviews(self):
        db = DatabaseManager('project.sql')
        query = """
        SELECT r.id, r.dish, r.rating, r.comment, u.username 
        FROM reviews r 
        JOIN users u ON r.user_id = u.id
        WHERE r.helpful IS NULL
        """
        criticism_reviews = db.search(query)
        db.close()

        self.ids.criticism_reviews.clear_widgets()
        for review in criticism_reviews:
            review_id, dish, rating, comment, username = review
            review_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
            review_box.add_widget(Label(
                text=f"User: {username}\nDish: {dish}\nRating: {rating}\nComment: {comment}",
                color=(0, 0, 0, 1),
                halign='left'
            ))
            helpful_btn = Button(
                text="Helpful",
                size_hint_y=None,
                height=30,
                on_release=lambda btn, rid=review_id: self.mark_helpful(rid)
            )
            unhelpful_btn = Button(
                text="Unhelpful",
                size_hint_y=None,
                height=30,
                on_release=lambda btn, rid=review_id: self.mark_unhelpful(rid)
            )
            review_box.add_widget(helpful_btn)
            review_box.add_widget(unhelpful_btn)
            self.ids.criticism_reviews.add_widget(review_box)

    def mark_helpful(self, review_id):
        db = DatabaseManager('project.sql')
        db.execute("UPDATE reviews SET helpful = TRUE WHERE id = ?", (review_id,))
        db.commit()
        db.close()
        self.load_criticism_reviews()

    def mark_unhelpful(self, review_id):
        db = DatabaseManager('project.sql')
        db.execute("UPDATE reviews SET helpful = FALSE WHERE id = ?", (review_id,))
        db.commit()
        db.close()
        self.load_criticism_reviews()

class ModeratorRestaurantApproval(Screen):
    def on_enter(self, *args):
        self.load_pending_restaurants()

    def load_pending_restaurants(self):
        db = DatabaseManager('project.sql')

        query_restaurants = """
        SELECT id, name, description, dishes
        FROM restaurants
        WHERE approved = FALSE
        """
        pending_restaurants = db.search(query_restaurants)

        self.ids.pending_restaurants.clear_widgets()

        for restaurant in pending_restaurants:
            restaurant_id, name, description, dishes = restaurant

            restaurant_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
            restaurant_box.add_widget(Label(
                text=f"Name: {name}\nDescription: {description}\nDishes: {dishes}",
                color=(0, 0, 0, 1),
                halign='left'
            ))

            approve_btn = Button(
                text="Approve",
                size_hint_y=None,
                height=30,
                on_release=lambda btn, rid=restaurant_id: self.approve_restaurant(rid)
            )
            reject_btn = Button(
                text="Reject",
                size_hint_y=None,
                height=30,
                on_release=lambda btn, rid=restaurant_id: self.reject_restaurant(rid)
            )
            restaurant_box.add_widget(approve_btn)
            restaurant_box.add_widget(reject_btn)

            self.ids.pending_restaurants.add_widget(restaurant_box)

        db.close()

    def approve_restaurant(self, restaurant_id):
        db = DatabaseManager('project.sql')

        try:
            query = "SELECT dishes FROM restaurants WHERE id = ?"
            result = db.search(query, (restaurant_id,))
            dishes_str = result[0][0]

            if not dishes_str:
                dishes = []
            else:
                dishes = [dish.strip() for dish in dishes_str.split(",")]

            db.execute("UPDATE restaurants SET approved = TRUE WHERE id = ?", (restaurant_id,))

            for dish in dishes:
                db.execute(
                    "INSERT INTO dishes (restaurant_id, name, spicy, sweet, savory) VALUES (?, ?, ?, ?, ?)",
                    (restaurant_id, dish, randint(0, 10), randint(0, 10), randint(0, 10))
            db.commit()
            print(f"Restaurant {restaurant_id} approved and dishes added to the dishes table.")
        except Exception as e:
            print(f"Error approving restaurant: {e}")
        finally:
            db.close()

        self.load_pending_restaurants()

    def reject_restaurant(self, restaurant_id):
        db = DatabaseManager('project.sql')
        db.execute("DELETE FROM restaurants WHERE id = ?", (restaurant_id,))
        db.commit()
        db.close()
        self.load_pending_restaurants()

class SignupScreen(Screen):
    selected_role = "User"

    def try_register(self):
        username = self.ids.uname.text.strip()
        email = self.ids.email.text.strip()
        passwd1 = self.ids.passwd1.text
        passwd2 = self.ids.passwd2.text
        role = self.ids.role_spinner.text

        if role == "Select Role":
            self.show_error("Please select a role.")
            return

        if role in ['Moderator', 'Admin']:
            self.show_error("Moderator and Admin roles cannot be selected for signup.")
            return

        if not username or not email or not passwd1 or not passwd2:
            self.show_error("All fields are required.")
            return

        if not self.validate_email(email):
            self.show_error("Please enter a valid email address.")
            return

        if len(passwd1) < 8:
            self.show_error("Password must be at least 8 characters long.")
            return

        if passwd1 != passwd2:
            self.show_error("Passwords do not match.")
            return

        db = DatabaseManager('project.sql')
        check_query = "SELECT * FROM users WHERE username = ? OR email = ?"
        result = db.search(check_query, (username, email))

        if result:
            self.show_error("Username or email already exists.")
            db.close()
            return

        insert_query = "INSERT INTO users (username, email, password, role, points) VALUES (?, ?, ?, ?, ?)"
        hashed_pass = hash_password(passwd1)
        db.execute(insert_query, (username, email, hashed_pass, role, 0))
        db.commit()

        user_id = db.search("SELECT id FROM users WHERE username = ?", (username,))[0][0]
        self.user_id = user_id

        if role == "Restaurant":
            restaurant_query = """
                INSERT INTO restaurants (name, description, owner_id, approved, sample)
                VALUES (?, ?, ?, ?, ?)
            """
            db.execute(restaurant_query, (
                "New Restaurant",
                "Description",
                user_id,
                False,
                False
            ))
            db.commit()

        db.close()
        print("User registered successfully!")

        if role == "Restaurant":
            print("Redirecting to restaurant home screen.")
            self.manager.current = 'restaurant_register'
        else:
            self.manager.current = 'login'

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def show_error(self, message):
        ErrorPopup(message).open()

class RestaurantDetailScreen(Screen):
    def load_restaurant(self, restaurant_id):
        self.restaurant_id = restaurant_id
        db = DatabaseManager('project.sql')

        query = "SELECT name, description, rating, photo FROM restaurants WHERE id = ?"
        restaurant = db.search(query, (restaurant_id,))[0]
        name, description, rating, photo = restaurant

        self.ids.restaurant_name.text = name
        self.ids.restaurant_description.text = description
        self.ids.restaurant_rating.text = f"Rating: {rating}"
        if photo:
            self.ids.restaurant_photo.source = photo
        else:
            self.ids.restaurant_photo.opacity = 0

        query = "SELECT name FROM dishes WHERE restaurant_id = ?"
        dishes = db.search(query, (restaurant_id,))
        self.ids.dish_spinner.values = [dish[0] for dish in dishes]

        query = "SELECT id, user_id, dish, rating, comment, likes, dislikes FROM reviews WHERE restaurant_id = ?"
        reviews = db.search(query, (restaurant_id,))
        db.close()

        self.ids.reviews_list.clear_widgets()
        for review in reviews:
            review_id, user_id, dish, rating, comment, likes, dislikes = review
            self.add_review_card(review_id, user_id, dish, rating, comment, likes, dislikes)

    def add_review_card(self, review_id, user_id, dish, rating, comment, likes, dislikes):
        print(f"Adding review card: Review ID={review_id}, Likes={likes}, Dislikes={dislikes}")

        likes = 0 if likes is None else likes
        dislikes = 0 if dislikes is None else dislikes

        review_card = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height="180dp",
            elevation=2,
            padding=10,
            spacing=10,
            md_bg_color=(1, 1, 1, 1))

        dish_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="30dp")
        dish_box.add_widget(Label(text=f"Dish: {dish}", font_size="14sp", color=(0, 0, 0, 1)))

        star_box = BoxLayout(orientation='horizontal', size_hint_x=None, width="150dp", spacing=5)

        full_stars = int(rating)
        half_star = 1 if (rating - full_stars) >= 0.5 else 0
        empty_stars = 5 - full_stars - half_star

        for _ in range(full_stars):
            star_box.add_widget(Image(source='fullstar.png', size_hint_x=None, width="20dp"))

        if half_star:
            star_box.add_widget(Image(source='star-half-icon.png', size_hint_x=None, width="20dp"))

        for _ in range(empty_stars):
            star_box.add_widget(Image(source='emptystar.png', size_hint_x=None, width="20dp"))

        dish_box.add_widget(star_box)

        comment_label = Label(text=comment, font_size="12sp", size_hint_y=None, height="60dp", color=(0, 0, 0, 1))

        like_dislike_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="30dp")

        like_box = BoxLayout(orientation='horizontal', size_hint_x=0.5, spacing=5)
        like_button = MDIconButton(
            icon="thumb-up",
            theme_text_color="Custom",
            text_color="green" if likes > 0 else (0.96, 0.98, 0.92, 1),
            on_release=lambda btn, rid=review_id: self.like_review(rid))
        like_button.review_id = review_id

        like_count_label = Label(
            text=str(likes),
            font_size="12sp",
            color=(0, 0, 0, 1))

        like_box.add_widget(like_button)
        like_box.add_widget(like_count_label)

        dislike_box = BoxLayout(orientation='horizontal', size_hint_x=0.5, spacing=5)
        dislike_button = MDIconButton(
            icon="thumb-down",
            theme_text_color="Custom",
            text_color="red" if dislikes > 0 else (0.96, 0.98, 0.92, 1),
            on_release=lambda btn, rid=review_id: self.dislike_review(rid))
        dislike_button.review_id = review_id

        dislike_count_label = Label(
            text=str(dislikes),
            font_size="12sp",
            color=(0, 0, 0, 1))

        dislike_box.add_widget(dislike_button)
        dislike_box.add_widget(dislike_count_label)

        like_dislike_box.add_widget(like_box)
        like_dislike_box.add_widget(dislike_box)

        review_card.add_widget(dish_box)
        review_card.add_widget(comment_label)
        review_card.add_widget(like_dislike_box)

        self.ids.reviews_list.add_widget(review_card)

    def like_review(self, review_id):
        print(f"Liking review {review_id}")
        db = DatabaseManager('project.sql')

        user_id = LoginScreen.current_user
        if not user_id:
            db.close()
            self.show_error("User not found. Please log in again.")
            return

        query = "SELECT likes, dislikes FROM reviews WHERE id = ?"
        result = db.search(query, (review_id,))
        print(f"Current likes/dislikes: {result}")

        if not result:
            db.close()
            return

        likes, dislikes = result[0]

        likes = 0 if likes is None else likes
        dislikes = 0 if dislikes is None else dislikes

        if dislikes > 0:
            db.execute("UPDATE reviews SET dislikes = dislikes - 1, likes = likes + 1 WHERE id = ?", (review_id,))
        elif likes == 0:
            db.execute("UPDATE reviews SET likes = likes + 1 WHERE id = ?", (review_id,))
        else:
            db.execute("UPDATE reviews SET likes = likes - 1 WHERE id = ?", (review_id,))

        db.commit()
        db.close()
        self.refresh_reviews()

    def dislike_review(self, review_id):
        db = DatabaseManager('project.sql')

        user_id = LoginScreen.current_user
        if not user_id:
            db.close()
            self.show_error("User not found. Please log in again.")
            return

        query = "SELECT likes, dislikes FROM reviews WHERE id = ?"
        result = db.search(query, (review_id,))
        if not result:
            db.close()
            return

        likes, dislikes = result[0]

        likes = 0 if likes is None else likes
        dislikes = 0 if dislikes is None else dislikes

        if likes > 0:
            db.execute("UPDATE reviews SET likes = likes - 1, dislikes = dislikes + 1 WHERE id = ?", (review_id,))
        elif dislikes == 0:
            db.execute("UPDATE reviews SET dislikes = dislikes + 1 WHERE id = ?", (review_id,))
        else:
            db.execute("UPDATE reviews SET dislikes = dislikes - 1 WHERE id = ?", (review_id,))

        db.commit()
        db.close()
        self.refresh_reviews()

    def refresh_reviews(self):
        self.ids.reviews_list.clear_widgets()
        self.load_restaurant(self.restaurant_id)

    def check_for_inappropriate_content(self, comment):
        INAPPROPRIATE_WORDS = ["terrible", "awful", "disgusting", "hate", "idiot", "stupid", "crap", "hell", "damn"]
        SWEAR_WORDS = ["fuck", "shit", "asshole", "bitch", "bastard", "dick", "piss", "cunt"]

        for word in SWEAR_WORDS:
            if word in comment.lower():
                return f"Contains inappropriate language: '{word}'"

        for phrase in INAPPROPRIATE_WORDS:
            if phrase in comment.lower():
                return f"Contains inappropriate phrase: '{phrase}'"

        import re
        LINK_PATTERN = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if LINK_PATTERN.search(comment):
            return "Contains links"

        try:
            rating = float(self.ids.rating_input.text)
            if rating == 1:
                return "Low rating"
        except ValueError:
            pass

        return None

    def add_review(self):
        dish = self.ids.dish_spinner.text
        rating = self.ids.rating_input.text
        comment = self.ids.comment_input.text

        if not dish or not rating or not comment:
            self.show_error("Please fill in all fields.")
            return

        try:
            rating = float(rating)
            if rating < 1 or rating > 5:
                self.show_error("Rating must be between 1 and 5.")
                return
        except ValueError:
            self.show_error("Rating must be a number.")
            return

        flagged_reason = self.check_for_inappropriate_content(comment)
        if flagged_reason:
            self.show_error(
                f"Your message was flagged as inappropriate and was sent for review. Reason: {flagged_reason}. TasteTogether is a platform for collaboration, sharing experiences, and improving the food industry. Help us keep our safe space!")
            self.send_for_review(dish, rating, comment, flagged_reason)
            return

        db = DatabaseManager('project.sql')

        user_id = LoginScreen.current_user
        if not user_id:
            db.close()
            self.show_error("User not found. Please log in again.")
            return

        query = "INSERT INTO reviews (restaurant_id, user_id, dish, rating, comment) VALUES (?, ?, ?, ?, ?)"
        db.execute(query, (self.restaurant_id, user_id, dish, rating, comment))

        self.update_restaurant_rating(self.restaurant_id, rating)

        db.close()

        self.ids.dish_spinner.text = "Select Dish"
        self.ids.rating_input.text = ""
        self.ids.comment_input.text = ""

        self.load_restaurant(self.restaurant_id)

    def update_restaurant_rating(self, restaurant_id, new_rating):
        db = DatabaseManager('project.sql')
        db.execute("UPDATE restaurants SET rating = ? WHERE id = ?", (new_rating, restaurant_id))
        db.commit()
        db.close()

    def show_error(self, message):
        ErrorPopup(message).open()

    def send_for_review(self, dish, rating, comment, reason):
        db = DatabaseManager('project.sql')

        user_id = LoginScreen.current_user
        if not user_id:
            db.close()
            self.show_error("User not found. Please log in again.")
            return

        query = """
            INSERT INTO flagged_reviews (restaurant_id, user_id, dish, rating, comment, reason)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        db.execute(query, (self.restaurant_id, user_id, dish, rating, comment, reason))
        db.commit()
        db.close()

class MDBottomNavigation:
    pass

class MultiRoleLoginApp(MDApp):
    def build(self):
        print("Building App...")
        self.create_database()

        try:
            return Builder.load_file('auth.kv')
        except Exception as e:
            print(f"Error loading KV file: {e}")
            return

    def create_database(self):
        print("Creating database...")
        db = DatabaseManager(name="project.sql")

        query_table_users = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT
        );
        """
        query_table_restaurants = """
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            rating REAL,
            photo TEXT
        );
        """
        query_table_reviews = """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            user_id INTEGER,
            dish TEXT,
            rating REAL,
            comment TEXT
        );
        """
        query_table_dishes = """
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            sweet REAL DEFAULT 0,
            salty REAL DEFAULT 0,
            sour REAL DEFAULT 0,
            bitter REAL DEFAULT 0,
            umami REAL DEFAULT 0
        );
        """
        query_table_user_taste_profiles = """
        CREATE TABLE IF NOT EXISTS user_taste_profiles (
            user_id INTEGER,
            sweet REAL DEFAULT 0,
            salty REAL DEFAULT 0,
            sour REAL DEFAULT 0,
            bitter REAL DEFAULT 0,
            umami REAL DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """
        db.save(query_table_users)
        db.save(query_table_restaurants)
        db.save(query_table_reviews)
        db.save(query_table_dishes)
        db.save(query_table_user_taste_profiles)

        query = "SELECT COUNT(*) FROM dishes"
        if db.search(query)[0][0] == 0:
            sample_dishes = [
                ("Chocolate Cake", 0.9, 0.1, 0.2, 0.1, 0.0),
                ("Salted Caramel Ice Cream", 0.7, 0.8, 0.1, 0.0, 0.0),
                ("Lemon Tart", 0.6, 0.1, 0.9, 0.2, 0.0),
                ("Dark Chocolate", 0.5, 0.1, 0.1, 0.9, 0.0),
                ("Miso Soup", 0.1, 0.6, 0.0, 0.1, 0.9)
            ]
            for name, sweet, salty, sour, bitter, umami in sample_dishes:
                query = "INSERT INTO dishes (name, sweet, salty, sour, bitter, umami) VALUES (?, ?, ?, ?, ?, ?)"
                db.execute(query, (name, sweet, salty, sour, bitter, umami))

        db.close()

if __name__ == '__main__':
    MultiRoleLoginApp().run()

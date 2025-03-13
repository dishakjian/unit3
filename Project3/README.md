# TasteTogether
![Sad Sponge Bob GIF by SpongeBob SquarePants](https://github.com/user-attachments/assets/0c9d952c-ccd0-4e00-8712-473be488973d)

# Criterion A
## Problem definition

Ms U, a food influencer, relies on honest and high-quality reviews to guide her audience. She is frustrated by unreliable ratings, fake reviews, and a lack of personalization in current food critique platforms. Many platforms allow users to rate restaurants without proof of visit, making it easy for trolls, bots, and competitors to manipulate ratings, ultimately reducing credibility. Additionally, current food rating platforms fail to consider individual taste preferences when recommending restaurants or dishes, leading to irrelevant suggestions that do not align with a user's culinary interests. On top of that, limited sorting options prevent users from filtering restaurants based on specific needs such as price range, culinary interests, popularity, or dietary restrictions, restricting their ability to find the best dining experiences efficiently. Another major issue is that users who take the time to write detailed and thoughtful reviews receive little to no recognition, discouraging engagement and lowering the overall quality of contributions.

As a food influencer, Ms. U frequently collaborates with restaurants and producers, gaining insight into their operational challenges. Restaurants rely on customer feedback to refine their offerings, yet they often struggle to extract meaningful insights from unstructured or misleading reviews. Without a way to engage with credible critiques, they face difficulty in addressing genuine concerns while filtering out bad-faith criticism. Meanwhile, food producers play a crucial role in maintaining quality and sustainability in the industry, but their lack of involvement in existing review ecosystems makes it hard for them to adapt to restaurant demands. Ms. U sees how these gaps in communication and credibility negatively impact both businesses and consumers, reinforcing the need for a more interconnected and transparent system that benefits the entire food industry.

(See evidence of Consultation in Appendix)

## Proposed solution

I chose to develop a desktop application over a website for its stability, performance, and security. Unlike web applications, which require constant internet connectivity and can suffer from network latency, and depends on a server, a desktop app processes data locally, handles large datasets, reducing wait times and improving user experience [[1]](https://www.ifourtechnolab.com/blog/web-app-vs-desktop-app#:~:text=Desktop%20apps%20usually%20offer%20better,you%20prioritize%20speed%20or%20convenience.) [[2]](https://builtbright.io/en/magazine/web-vs-desktop-applications-pros-and-cons/). It also provides enhanced security by enforcing stricter access controls and local encryption, avoiding vulnerabilities like cross-site scripting and SQL injection [[3]](https://www.softwareseni.com/identifying-and-assessing-risks-in-web-and-app-development/) [[4]](https://rubygarage.org/blog/risk-management-in-development).

I chose Python for GUI development due to its readability and cross platform compatibility, making understanding and future modifications easier for stakeholders [[5]](https://serokell.io/blog/python-pros-and-cons) [[6]](https://www.geeksforgeeks.org/python-language-advantages-applications/). It is also lightweight compared to lower-level languages like C++ and Java, ensuring efficiency without unnecessary complexity [[7]](https://www.snaplogic.com/glossary/python-vs-java-performance) [[8]](https://lset.uk/blog/unveiling-the-future-of-python-exploring-the-latest-trends-and-innovations-in-2023-and-beyond/) [[9]](https://blog.jetbrains.com/pycharm/2023/10/future-of-data-science/). 

I chose KivyMD because it provides a modern, visually appealing, and user-friendly interface based on Google’s Material Design [[10]](https://kivymd.readthedocs.io/en/latest/) [[11]](https://m2.material.io/design/introduction/). It ensures a smooth and consistent experience across devices, making navigation intuitive and interactions seamless. Unlike **Tkinter**, which has a basic and outdated appearance, KivyMD offers a polished and engaging design that enhances usability[[12]](https://kivy.org/#home) [[13]](https://medium.com/@qasim.coder/python-gui-smackdown-unleashing-the-power-of-tkinter-pyqt-and-kivy-e7b05d0e862).

I chose SQLite for data storage because it is lightweight, serverless, and cost-effective while efficiently handling structured data like user reviews and restaurant details [[14]](https://www.sqlite.org/whentouse.html) [[15]](https://www.epicweb.dev/why-you-should-probably-be-using-sqlite) [[16]](https://www.sqlite.org/aff_short.html). Unlike **MySQL** or **PostgreSQL**, which require a dedicated server and maintenance, SQLite operates locally with minimal setup, making it ideal for a fast and seamless user experience [[17]](https://www.greengeeks.com/blog/sqlite-vs-mysql/#:~:text=Ultimately%2C%20SQLite%20is%20a%20lightweight,go%2Dto%20for%20RDBMS%20solutions.).

## Success criteria
[success criteria (2).pdf](https://github.com/user-attachments/files/19197099/success.criteria.2.pdf)

(See evidence of Approval in Appendix)

## References (for Criterion A)

1. iFour Technolab. "Web App vs. Desktop App." [https://www.ifourtechnolab.com/blog/web-app-vs-desktop-app](https://www.ifourtechnolab.com/blog/web-app-vs-desktop-app#:~:text=Desktop%20apps%20usually%20offer%20better,you%20prioritize%20speed%20or%20convenience.)
2. Built Bright. "Web vs. Desktop Applications: Pros and Cons." [https://builtbright.io/en/magazine/web-vs-desktop-applications-pros-and-cons/](https://builtbright.io/en/magazine/web-vs-desktop-applications-pros-and-cons/)
3. Software Seni. "Identifying and Assessing Risks in Web and App Development." [https://www.softwareseni.com/identifying-and-assessing-risks-in-web-and-app-development/](https://www.softwareseni.com/identifying-and-assessing-risks-in-web-and-app-development/)
4. Ruby Garage. "Risk Management in Development." [https://rubygarage.org/blog/risk-management-in-development](https://rubygarage.org/blog/risk-management-in-development)
5. Serokell. "Python: Pros and Cons." [https://serokell.io/blog/python-pros-and-cons](https://serokell.io/blog/python-pros-and-cons)
6. GeeksforGeeks. "Python Language Advantages & Applications." [https://www.geeksforgeeks.org/python-language-advantages-applications/](https://www.geeksforgeeks.org/python-language-advantages-applications/)
7. SnapLogic. "Python vs Java Performance." [https://www.snaplogic.com/glossary/python-vs-java-performance](https://www.snaplogic.com/glossary/python-vs-java-performance)
8. LSET. "Unveiling the Future of Python: Exploring the Latest Trends and Innovations in 2023 and Beyond." [https://lset.uk/blog/unveiling-the-future-of-python-exploring-the-latest-trends-and-innovations-in-2023-and-beyond/](https://lset.uk/blog/unveiling-the-future-of-python-exploring-the-latest-trends-and-innovations-in-2023-and-beyond/)
9. JetBrains. "The Future of Data Science." [https://blog.jetbrains.com/pycharm/2023/10/future-of-data-science/](https://blog.jetbrains.com/pycharm/2023/10/future-of-data-science/)
10. KivyMD Documentation. [https://kivymd.readthedocs.io/en/latest/](https://kivymd.readthedocs.io/en/latest/)
11. Google Material Design. [https://m2.material.io/design/introduction/](https://m2.material.io/design/introduction/)
12. Kivy. "Kivy: Open Source Python Library for Rapid Development." [https://kivy.org/#home](https://kivy.org/#home)
13. Medium. "Python GUI Smackdown: Tkinter, PyQt, and Kivy." [https://medium.com/@qasim.coder/python-gui-smackdown-unleashing-the-power-of-tkinter-pyqt-and-kivy-e7b05d0e862](https://medium.com/@qasim.coder/python-gui-smackdown-unleashing-the-power-of-tkinter-pyqt-and-kivy-e7b05d0e862)
14. SQLite. "Appropriate Uses for SQLite." [https://www.sqlite.org/whentouse.html](https://www.sqlite.org/whentouse.html)
15. Epic Web Dev. "Why You Should Probably Be Using SQLite." [https://www.epicweb.dev/why-you-should-probably-be-using-sqlite](https://www.epicweb.dev/why-you-should-probably-be-using-sqlite)
16. SQLite. "Short History of SQLite." [https://www.sqlite.org/aff_short.html](https://www.sqlite.org/aff_short.html)
17. GreenGeeks. "SQLite vs MySQL." [https://www.greengeeks.com/blog/sqlite-vs-mysql](https://www.greengeeks.com/blog/sqlite-vs-mysql/#:~:text=Ultimately%2C%20SQLite%20is%20a%20lightweight,go%2Dto%20for%20RDBMS%20solutions.)


# Criterion B
## Systems Diagram
![systemdiagramp3](https://github.com/user-attachments/assets/8d04a37c-fdb2-499a-8d6e-a81207d536f9)

Fig. 1, solution's hardware and software components and interactions

## Flow Diagrams

![Blank diagram (6)](https://github.com/user-attachments/assets/a54e8d8e-64d3-4ec6-a8d4-ebb255b728d0)

Fig. 2, flow diagram for filter_restaurants

![Blank diagram (8)](https://github.com/user-attachments/assets/a01d0984-7e9e-4fa5-89c9-9a34661cd519)

Fig. 3, flow diagram for add_review (includes flow diagram for check_for_inappropriate_content)

![Blank diagram (7)](https://github.com/user-attachments/assets/fb18d51b-4382-48fe-ab43-8972f9b802e9)

Fig. 4, flow diagram for try_login

## Wireframe diagram

![Blank diagram (10)](https://github.com/user-attachments/assets/21530be2-fc6f-4269-bdee-c80ff421f384)

Fig. 5, wireframe diagram for screen management and buttons

## UML Diagram

![Flowchart (6)](https://github.com/user-attachments/assets/343400d1-ddca-4ed8-a9e5-0f37a81a4c2f)

Fig. 6, UML Class Diagram for classes in project

## ER Diagram

![Blank diagram (9)](https://github.com/user-attachments/assets/8c54568c-473e-40dd-a91f-f2a04d282189)

Fig. 7, ER Diagram detailing entity-relationships (showing how entities relate to each other within the project system).

## Data Storage
Tables in my SQL file

![image](https://github.com/user-attachments/assets/f0731882-50ea-4bf9-8e53-532d343266fe)

Fig. 8, 10 tables in database (2 default)

### Extracts of data storage in each table

![image](https://github.com/user-attachments/assets/1f7b9355-a16e-4bf3-94c4-b92b42c19558)

Fig. 9, Data storage in table dishes

![image](https://github.com/user-attachments/assets/d2f3029d-7044-4b4d-b5e7-d838c69efe9e)

Fig. 10, Data storage in flagged_reviews

![image](https://github.com/user-attachments/assets/1c1db38b-d4d5-4009-939e-82280475c73c)

Fig. 11, Data storage in inventory

![image](https://github.com/user-attachments/assets/a2989da6-25a8-4085-9e0c-91824992080b)

Fig. 12, Data storage in requests

![image](https://github.com/user-attachments/assets/dae1a027-b078-4c42-822f-303f065f264e)

Fig. 13, Data storage in restaurants

![image](https://github.com/user-attachments/assets/5c1c6ac9-76ef-4473-b0a4-cb8c27bc5c19)

Fig. 14, Data storage in reviews

![image](https://github.com/user-attachments/assets/30ed05a6-ceb2-48a9-93c6-4bfd5aa87445)

Fig. 15, Data storage in users

![image](https://github.com/user-attachments/assets/4c7a6282-6154-4fa2-8c81-ec00db9852c7)

Fig. 16, Data storage in user_taste_profiles

## Record of Tasks
| Task No | Planned Action | Planned Outcome | Time Estimate (min) | Target Completion Date | Criteria |
|---------|---------------|-----------------|--------------------|----------------------|----------|
| 1 | Consultation with client | Interview client, take notes, and define the problem | 30 | Jan 30 | A |
| 2 | Rejected proposal from client, suggested improvements | Adjust project direction based on client feedback | - | Jan 30 | A |
| 3 | Accepted new client proposal | Finalize new project scope | - | Jan 31 | A |
| 4 | Write problem definition | Based on consultation notes, finalize a description of the problem. | 30 | Jan 31 | A |
| 5 | Write proposed solution | Finalize the success criteria and form a proposed solution to justify the methods that will be used. | 40 | Feb 1 | A |
| 6 | Write success criteria | Create success criteria and get approval from the client | 40 | Feb 1 | A |
| 7 | Research on the best way to create a GUI application and videos about the program I will be using | A clear understanding of the best way to create a GUI application | 120 | Feb 1 | A |
| 8 | Research on the best way to create a database | A clear understanding of the best way to create a database | 60 | Feb 1 | A |
| 9 | Edit success criteria | Edit success criteria based off newly gained knowledge, expectations, and predictions | 20 | Feb 1 | A |
| 10 | Send success criteria | Share proposed success criteria with client | - | Feb 1 | A |
| 11 | Approve success criteria | Receive client approval | - | Feb 4 | A |
| 12 | Set up the database | A database that is ready to be used | 90 | Feb 20 | C |
| 13 | Create basic screens and link them | Build structure of application | 60 | Feb 22 | C/D |
| 14 | Create welcome screen and login/signup screens | Allow user (role-based access) authentication via database | 60 | Feb 24 | C/D |
| 15 | Create home screen for each role | Enable navigation through the application | 240 | Feb 28 | C |
| 16 | Create extra screens for each role | Allow admin to manage employees | 180 | Mar 3 | C/D |
| 17 | Modify database, add sample data | More tables and relevant columns, sample data for each to test and add information | 90 | Mar 5 | C/D |
| 18 | Run tests | Identify and fix screen management, widgets, and connection issues | 60 | Mar 5 | B/C/D |
| 19 | Change KivyMD version for better UI/UX and functionality | Ensure better design and functionality | 240 | Mar 6 | C/D |
| 20 | Run tests | Identify and fix functionality and compatibility issues | 60 | Mar 6 | B/C/D |
| 21 | Create wireframe | Plan the frontend structure of the application | 120 | Mar 8 | B |
| 22 | Create ER diagram | Understand the structure of the database needed | 90 | Mar 8 | B |
| 23 | Create UML diagram | Understand the classes needed for the final application | 30 | Mar 8 | B |
| 24 | Create system diagram | Plan the deployment of the final application | 60 | Mar 8 | B |
| 25 | Create test plan | Establish a test strategy for verification | 15 | Mar 9 | B |
| 26 | Run full tests | Identify and fix functionality issues | 20 | Mar 9 | B/C/D |
| 27 | Documentation | Documenting existing tools and sources used for developing the program | 180 | Mar 10 | C |
| 28 | Adjust and finalize UI | Improve user-friendliness and aesthetics | 90 | Mar 10 | C/D |
| 29 | Run final tests | Ensure all changes did not break functionality | 30 | Mar 10 | C |
| 30 | Film video | A video detailing the program while following the test plan | 30 | Mar 11 | D |
| 31 | Final adjustments and documentation | Ensure project is well-documented | 60 | Mar 11 | A/B/C/D |

## Test Plan

| **Success Criteria**                     | **Description**                                                                 | **Test Procedure**                                                                                                                                                                                                 | **Expected Outcome**                                                                                   |
|------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 1. Secure Multi-role login system| A secure authentication system will be implemented to ensure that users, restaurants, moderators, and producers have different access levels and functionalities. Each user type will have role-based access, ensuring secure data handling and preventing unauthorized actions.| 1. Run project.py 2. Find and check the terms and conditions box 3. Find and click SIGN UP button 4. Click on respective text box and enter a unique username (eg. Bob), valid email (eg. bob@hotmail.com), and a password at least 8 letters (eg. 12345678), then that same password again in confirm password (eg. 12345678) 5. Find DropDown menu and select a role (eg. User). 6. Find and click "Sign up". 7. Click on respective text box and enter the same details as in Sign up (eg. Bob for username, 12345678 for password) 8. Find DropDown menu and select the same role as in Sign up (eg. User) 9. Find and click Log in| User is registered, and the database stores the hashed password. Redirects to the login. Redirects to home screen. |
| 2. Personalization | The platform will predict whether a user will enjoy a dish based on their taste profile and past reviews, improving recommendation accuracy and ensuring that feedback is relevant to the user’s preferences. | 1. Run project.py 2. Find and check the terms and conditions box. 3. Find and click LOG IN button. 4. Find and click respective text boxes to enter the folllowing information (past reviews and taste profile is needed for recommendation) Username: jane_smith, Password: 12345678 5. Find and click LOG IN button 6. Find and click DropDown filters next to the search bar on the top of the screen. 7. Select rating 8. See restaurants and ranking 9. Find and click Dropdown filters again 10. Select recommended 11. See difference in restaurants and ranking. | Ranking based on user's previous reviews and taste profile from those reviews.|
| 3. Moderation | An automated system with a blacklist will flag inappropriate reviews containing offensive language, spam, or misleading content, for the moderators to review and delete if necessary. | 1. Complete steps 1-9 from test 1 or 1-4 from test 2 (Username: Bob, Password: 12345678) if steps 1-9 from test 1 have already been tested 2. Find and select view details button of any restaurant (eg. Burger King). 3. Find and click dropdown dishes, select any (eg. Whopper) 4. Click on Rating text box, type a rating (eg. 2). 5. Click on Comment text box, type an inappropriate comment including swear words (eg. "Tastes like shit"). 6. Find and click Submit Review button. 7. Read Pop up dialogue. 8. Find and click back arrow button. 9. Find and click logout button in bottom navigation. 10. Click on username text box and type "mod1" 11. Click on password text box and type "12345678". 12. Find and click on the Role dropdown and select "Moderator". 13. Find and click LOG IN button. 14. Scroll down screen. 15. Find newly flagged review at the bottom. 16. Find and click delete button. | Review is not published, flagged, and sent to moderators for review. Moderator can view the flagged review and approve or delete it. |
| 4. Review Management | Users can leave reviews for restaurants including dish name, rating, and comment. Restaurant owners can view categorized reviews for their restaurant. | 1. Complete steps 1-3 from test 3. 4. Click on Rating text box, type a rating (eg. 5). 5. Click on comment text box, type a comment (eg. "I really enjoyed the meal and atmosphere"). 6. Find and click Submit Review button. 7. Complete steps 8-12 from test 12. Find and click second item in the bottom navigation, "restaurant reviews". 13. Scroll down to find newly added review. 14. Click on button Helpful. 15. Find and click logout button in bottom navigation. 16. Find and click the username text box, type the name of the restaurant you added a review on in steps 1-6 (eg. BurgerKing). 17. Find and click the password text box, type the password "12345678". 18. Scroll to find newly added and categorized review. | Review is published including dish name, rating, and comment. Moderators can categorize reviews based on Helpful or Unhelpful traits. Restaurant owners can view all reviews left on their restaurant, with a comment from the Moderator about Helpfulness.|
| 5. Restaurant <-> Producers Network | The platform will facilitate direct collaboration between restaurants and food producers, allowing restaurants to request specific ingredient quantities with a set budget and producers will choose between sustainable and cost-effective sourcing options. Producers will have a transparent marketplace to connect with buyers, improving supply chain efficiency.| 1. Run project.py 2. Find and check the terms and conditions box. 3. Find and click the LOG IN button. 4. Find and click on username text box and type restaurant username login, (eg. "MOSBURGER"). 5. Find and click on password text box and type restaurant password login, (eg. "12345678"). 6. Find and click on dropdown role menu. 7. Click on Restaurant from dropdown role menu. 8. Find and click on LOG IN button. 9. Find navigation bar on the bottom of the screen and navigate to the second screen, inventory, by clicking on the second icon in the bottom navigation. 10. See restaurant inventory. 11. Find and click "Request from Producer" button. 12. From "Select Producer "dropdown menu, select any producer (eg. GreenView). 13. Find and click textbox "item" and type the name of the desired item to refill or add, (eg. Tomatoes). 14. Find and click textbox "item" and type the set budget (eg. 1000). 15. Find and click the "SUBMIT" button. 16. From the bottom navigation on the bottom of the screen, click the third button, the logout icon to log out. 17. Find and click on the role dropdown menu. 18. Click on Producer from dropdown menu. 19. Find and click textbox username and type in Producer username login (eg. GreenView). 20. Find and click textbox password and type in Producer login password (eg. 12345678). 21. Find and click "LOG IN" button. 22. Scroll to bottom to find newly sent request. 23. Choose one of the options generated by clicking on the relevant button. 24. From the bottom navigation on the bottom of the screen, click the only available option, the logout button, to log out. 25. Repeat steps 4-10 26. See update in restaurant inventory | Restaurants can request specific ingredient quantities with a set budget. Producers can choose between sustainable, cost-effective, and a "middle-ground" sourcing option. They have a transparent marketplace to connect with each other.|


# Criterion C

## LIST OF TECHNIQUES  

### 1. Database Management Techniques  
- CRUD Operations  
- Database Normalization  
- Foreign Key Relationships  
- Transaction Management  
- Query Optimization  

### 2. User Authentication and Authorization  
- Password Hashing  
- Role-Based Access Control (RBAC)  
- Session Management  

### 3. Data Filtering and Sorting  
- Dynamic Filtering  
- Custom Sorting Algorithms  
- Search Functionality  

### 4. Personalization and Recommendation Systems  
- Taste Profiling  
- Recommendation Scoring  
- Dynamic UI Updates  

### 5. Error Handling and Validation  
- Input Validation  
- Inappropriate Content Detection  
- Error Popups  
- Exception Handling  

### 6. Moderation and Flagging Systems  
- Flagging Mechanism  
- Approval/Rejection Workflow  
- Audit Trail  

### 7. UI/UX Design Techniques  
- Dynamic Card Creation  
- Interactive Widgets  
- Progress Indicators  
- Popup Dialogs  

### 8. Data Aggregation and Reporting  

### 9. Algorithm Design  
- Weighted Scoring  
- Randomization  
- Sorting Algorithms  

### 10. Security Techniques  
- Data & Input Sanitization  
- Role-Based Permissions  

### 11. Code Organization and Modularity  
- Reusable Components  
- Comments and Documentation  
- Database Abstraction  

### 12. Testing and Debugging Techniques  
- Debugging Statements  
- Error Logging  
- Validation Testing  

### 13. User Feedback and Interaction  
- Like/Dislike System  
- Review Moderation Feedback  
- Progress Tracking  

### 14. Data Visualization  

### 15. Event-Driven Programming  
- Button Click Handling  
- Screen Transition Handling  

### 16. Data Persistence  
- Local Database Storage  
- Session Persistence  


## Filter Restaurants function
This function is responsible for filtering and sorting restaurants based on user preferences and displaying them in a user-friendly format. It handles three main filtering options: Price, Rating, and Recommended. The Recommended filter uses the user's taste profile to calculate a personalized recommendation score for each restaurant. Additionally, it supports a search query to filter restaurants by name or description.

```.py
def filter_restaurants(self):
    # I start by retrieving the filter type selected by the user from the filter_spinner widget.
    filter_type = self.ids.filter_spinner.text

    # I also get the search query entered by the user from the search_input widget and convert it to lowercase for case-insensitive matching.
    search_query = self.ids.search_input.text.lower()

    # I open a connection to the SQLite database using the DatabaseManager class to fetch restaurant data.
    db = DatabaseManager('project.sql')

    # I define a SQL query to select all restaurants' details: id, name, description, rating, price, and photo.
    query = "SELECT id, name, description, rating, price, photo FROM restaurants"

    # I execute the query and store the results in the `restaurants` variable, which will contain a list of tuples.
    restaurants = db.search(query)

    # I close the database connection to free up resources and avoid potential memory leaks.
    db.close()

    # I print the number of restaurants found to the console for debugging purposes.
    print(f"Found {len(restaurants)} restaurants.")

    # I clear the existing restaurant cards from the restaurant_list widget to prepare for displaying the filtered results.
    self.ids.restaurant_list.clear_widgets()

    # I check the filter type selected by the user to determine how to sort the restaurants.
    if filter_type == 'Price':
        # If the filter type is 'Price', I sort the restaurants by their price. 
        # The price is represented by the number of '¥' symbols in the 4th index of the tuple.
        # If the price is None, I default it to 0 to avoid errors during sorting.
        restaurants.sort(key=lambda x: x[4] if x[4] is not None else 0)
    elif filter_type == 'Rating':
        # If the filter type is 'Rating', I sort the restaurants by their rating.
        # The rating is in the 3rd index of the tuple. If it's None, I default it to 0.
        # I sort in descending order (reverse=True) so higher-rated restaurants appear first.
        restaurants.sort(key=lambda x: x[3] if x[3] is not None else 0, reverse=True)
    elif filter_type == 'Recommended':
        # If the filter type is 'Recommended', I need to calculate a recommendation score for each restaurant based on the user's taste profile.
        # I reopen the database connection to fetch the user's taste profile.
        db = DatabaseManager('project.sql')

        # I query the database to get the user's ID using their username stored in LoginScreen.current_username.
        user_id = db.search("SELECT id FROM users WHERE username = ?", (LoginScreen.current_username,))[0][0]

        # I fetch the user's taste profile (sweet, salty, sour, bitter, umami) from the user_taste_profiles table.
        user_taste_profile = db.search(
            "SELECT sweet, salty, sour, bitter, umami FROM user_taste_profiles WHERE user_id = ?",
            (user_id,))
        
        # I close the database connection after fetching the data.
        db.close()

        # If the user has a taste profile, I proceed to calculate recommendation scores for each restaurant.
        if user_taste_profile:
            # I unpack the taste profile values into individual variables for easier calculation.
            user_sweet, user_salty, user_sour, user_bitter, user_umami = user_taste_profile[0]

            # I iterate over each restaurant to calculate its recommendation score.
            for i, restaurant in enumerate(restaurants):
                # I get the restaurant's ID from the first element of the tuple.
                restaurant_id = restaurant[0]

                # I calculate the restaurant's taste profile by calling the `calculate_restaurant_taste_profile` method.
                restaurant_taste_profile = self.calculate_restaurant_taste_profile(restaurant_id)

                # If the restaurant has no taste profile, I append a default score of 0.0 and skip further calculations.
                if not restaurant_taste_profile:
                    # I convert the tuple to a list to append the score, then convert it back to a tuple.
                    restaurant = list(restaurant)
                    restaurant.append(0.0)
                    restaurants[i] = tuple(restaurant)
                    continue

                # I calculate the recommendation score by multiplying the user's taste preferences with the restaurant's taste profile.
                recommendation_score = (
                        user_sweet * restaurant_taste_profile["sweet"] +
                        user_salty * restaurant_taste_profile["salty"] +
                        user_sour * restaurant_taste_profile["sour"] +
                        user_bitter * restaurant_taste_profile["bitter"] +
                        user_umami * restaurant_taste_profile["umami"]
                )

                # I append the recommendation score to the restaurant tuple by converting it to a list, appending the score, and converting it back to a tuple.
                restaurant = list(restaurant)
                restaurant.append(recommendation_score)
                restaurants[i] = tuple(restaurant)

            # I sort the restaurants by their recommendation score in descending order so the most recommended restaurants appear first.
            restaurants.sort(key=lambda x: x[-1], reverse=True)

    # I filter the restaurants based on the search query entered by the user.
    filtered_restaurants = []
    for restaurant in restaurants:
        # I unpack the restaurant tuple into individual variables for easier access.
        restaurant_id, name, description, rating, price, photo, *rest = restaurant

        # I check if the search query is empty or if it matches the restaurant's name or description (case-insensitive).
        if not search_query or search_query in name.lower() or search_query in description.lower():
            # If the restaurant matches the search query, I add it to the filtered_restaurants list.
            filtered_restaurants.append(restaurant)

    # I iterate over the filtered restaurants to create and display a card for each one.
    for restaurant in filtered_restaurants:
        # I unpack the restaurant tuple again for clarity.
        restaurant_id, name, description, rating, price, photo, *rest = restaurant

        # I set a default price of 3 if the price is None.
        price = price if price is not None else 3

        # I print the restaurant's name to the console for debugging purposes.
        print(f"Creating card for: {name}")

        # I create a new MDCard widget to display the restaurant's details.
        card = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height="180dp",
            elevation=4,
            padding=10,
            spacing=10,
            md_bg_color=(1, 1, 1, 1))

        # I create a horizontal BoxLayout to hold the restaurant's name, rating, and price.
        title_box = BoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")

        # I create a Label widget to display the restaurant's name.
        title_label = Label(
            text=name,
            font_size="18sp",
            bold=True,
            size_hint_x=0.6,
            color=(0, 0, 0, 1))

        # I create another horizontal BoxLayout to display the star rating.
        rating_box = BoxLayout(orientation='horizontal', size_hint_x=0.2, spacing=5)

        # I calculate the number of full stars, half stars, and empty stars based on the restaurant's rating.
        rating = rating if rating is not None else 0  # Default to 0 if rating is None
        full_stars = int(rating)
        half_star = 1 if (rating - full_stars) >= 0.5 else 0
        empty_stars = 5 - full_stars - half_star

        # I add full star images to the rating_box.
        for _ in range(full_stars):
            rating_box.add_widget(Image(source='fullstar.png', size_hint=(None, None), size=(20, 20)))

        # I add a half star image if applicable.
        if half_star:
            rating_box.add_widget(Image(source='star-half-icon.png', size_hint=(None, None), size=(20, 20)))

        # I add empty star images to fill the remaining space.
        for _ in range(empty_stars):
            rating_box.add_widget(Image(source='emptystar.png', size_hint=(None, None), size=(20, 20)))

        # I create a Label widget to display the restaurant's price.
        price_label = Label(
            text=f"¥{'¥' * price}",
            font_size="16sp",
            size_hint_x=0.2,
            color=(0, 0, 0, 1))

        # I add the title_label, rating_box, and price_label to the title_box.
        title_box.add_widget(title_label)
        title_box.add_widget(rating_box)
        title_box.add_widget(price_label)

        # I create a Label widget to display the restaurant's description.
        description_label = Label(
            text=description,
            font_size="14sp",
            size_hint_y=None,
            height="60dp",
            color=(0, 0, 0, 1))

        # I create a Button widget to allow the user to view more details about the restaurant.
        details_button = Button(
            text="View Details",
            size_hint_y=None,
            height="40dp",
            on_release=lambda btn, rid=restaurant_id: self.view_restaurant(rid))

        # I add the title_box, description_label, and details_button to the card.
        card.add_widget(title_box)
        card.add_widget(description_label)
        card.add_widget(details_button)

        # I add the card to the restaurant_list widget to display it on the screen.
        self.ids.restaurant_list.add_widget(card)

        # I print the restaurant's name to the console to confirm the card was added.
        print(f"Added card for: {name}")
```

### How It Works - Summary

1. Data Retrieval: The function starts by fetching all restaurants from the database. It then clears the existing UI elements to prepare for displaying the filtered results.

2. Filtering and Sorting:
- If the user selects Price, the restaurants are sorted by their price (represented by the number of '¥' symbols).

- If the user selects Rating, the restaurants are sorted by their rating in descending order.

- If the user selects Recommended, the function calculates a recommendation score for each restaurant based on the user's taste profile and the restaurant's taste profile. The restaurants are then sorted by this score.

3. Search Query Filtering: After sorting, the function filters the restaurants based on the search query entered by the user. It checks if the query matches the restaurant's name or description (case-insensitive).

4. UI Rendering: For each filtered restaurant, the function creates a card that displays the restaurant's name, rating, price, and description. The card also includes a button to view more details about the restaurant.

5. Dynamic Updates: The function dynamically updates the UI to reflect the filtered and sorted results, ensuring a smooth user experience.

## Calculate Restaurant Taste Profile Function
This function calculates the taste profile of a restaurant based on the dishes in its reviews. The taste profile is used to provide personalized recommendations to users based on their taste preferences.

```.py
def calculate_restaurant_taste_profile(self, restaurant_id):
    """
    I calculate the taste profile for a restaurant based on the dishes in its reviews.
    """
    # I open a connection to the SQLite database using the DatabaseManager class.
    db = DatabaseManager('project.sql')
    try:
        # I define a SQL query to fetch the taste profiles of all dishes associated with the restaurant's reviews.
        query = """
        SELECT d.sweet, d.salty, d.sour, d.bitter, d.umami
        FROM reviews r
        JOIN dishes d ON r.dish = d.id
        WHERE r.restaurant_id = ?
        """
        # I execute the query and store the results in the `dish_taste_profiles` variable.
        dish_taste_profiles = db.search(query, (restaurant_id,))

        # If no dishes are found, I return a default taste profile with all values set to 0.
        if not dish_taste_profiles:
            return {
                "sweet": 0,
                "salty": 0,
                "sour": 0,
                "bitter": 0,
                "umami": 0,
            }

        # I initialize a dictionary to store the cumulative taste profile.
        taste_profile = {"sweet": 0, "salty": 0, "sour": 0, "bitter": 0, "umami": 0}

        # I iterate over each dish's taste profile to calculate the cumulative taste profile.
        for dish in dish_taste_profiles:
            # I unpack the taste attributes for the current dish.
            sweet, salty, sour, bitter, umami = dish

            # I add each taste attribute to the cumulative taste profile.
            taste_profile["sweet"] += sweet
            taste_profile["salty"] += salty
            taste_profile["sour"] += sour
            taste_profile["bitter"] += bitter
            taste_profile["umami"] += umami

        # I normalize the taste profile by dividing each attribute by the number of dishes.
        num_dishes = len(dish_taste_profiles)
        for key in taste_profile:
            taste_profile[key] /= num_dishes

        # I return the normalized taste profile.
        return taste_profile

    except Exception as e:
        # If an error occurs, I print the error message and return a default taste profile.
        print(f"Error calculating taste profile: {e}")
        return {
            "sweet": 0,
            "salty": 0,
            "sour": 0,
            "bitter": 0,
            "umami": 0,
        }
    finally:
        # I ensure the database connection is closed, even if an error occurs.
        db.close()
```
### How It Works - Summary
1. Data Retrieval: The function queries the database to fetch the taste profiles of all dishes associated with the restaurant's reviews.

2. Default Handling: If no dishes are found, it returns a default taste profile with all values set to 0.

3. Cumulative Calculation: It iterates over each dish's taste profile and calculates the cumulative taste profile by summing up the taste attributes.

4. Normalization: The cumulative taste profile is normalized by dividing each attribute by the number of dishes.

5. Error Handling: If an error occurs, it prints the error message and returns a default taste profile.

6. Resource Management: The database connection is closed in the finally block to ensure proper resource management.

## Try Login Function
This function handles user login by validating the username, password, and role entered by the user. It also checks if a restaurant user is approved before allowing access.

```.py
def try_login(self):
    # I retrieve the username, password, and role entered by the user from the UI.
    username = self.ids.uname.text
    password = self.ids.passwd.text
    role = self.ids.role_spinner.text

    # I check if the username or password fields are empty.
    if not username or not password:
        # If either field is empty, I show an error message and return.
        self.show_error("Please fill in all fields.")
        return

    # I define a SQL query to search for the user in the database.
    search_user = "SELECT id, username, email, password, role, points FROM users WHERE username = ? AND role = ?"
    # I open a connection to the SQLite database using the DatabaseManager class.
    db = DatabaseManager('project.sql')
    # I execute the query and store the result in the `result` variable.
    result = db.search(search_user, (username, role))

    # I check if exactly one user was found.
    if len(result) == 1:
        # I unpack the user's details from the result.
        user_id, username, email, stored_hash_password, role, points = result[0]

        # I check if the entered password matches the stored hash password.
        if check_hash(input_str=password, hash=stored_hash_password):
            # If the password matches, I store the user's ID and username in the LoginScreen class.
            LoginScreen.current_user = user_id
            LoginScreen.current_username = username

            # If the user is a restaurant, I check if the restaurant is approved.
            if role == "Restaurant":
                # I define a SQL query to fetch the restaurant's approval status.
                restaurant_query = "SELECT approved FROM restaurants WHERE owner_id = ?"
                # I execute the query and store the result in the `restaurant_result` variable.
                restaurant_result = db.search(restaurant_query, (user_id,))
                # I close the database connection.
                db.close()

                # If the restaurant is found, I check its approval status.
                if restaurant_result:
                    approved = restaurant_result[0][0]
                    # I redirect the user to the appropriate screen based on the approval status.
                    self.redirect_to_role_screen(role, approved)
                else:
                    # If the restaurant is not found, I show an error message.
                    self.show_error("Restaurant not found.")
                    return
            else:
                # For non-restaurant roles, I redirect the user directly.
                self.redirect_to_role_screen(role)
        else:
            # If the password does not match, I show an error message.
            db.close()
            self.show_error("Username or password incorrect.")
    else:
        # If no user is found, I show an error message.
        db.close()
        self.show_error("User not found.")
```
### How It Works - Summary
1. Input Validation: The function checks if the username and password fields are filled.

2. Database Query: It queries the database to find a user with the entered username and role.

3. Password Verification: It verifies the entered password against the stored hash password.

4. Role Handling: If the user is a restaurant, it checks if the restaurant is approved before redirecting.

5. Error Handling: It shows appropriate error messages for invalid inputs or database errors.

6. Redirection: It redirects the user to the appropriate screen based on their role and approval status.

## Add Reviews Function
This function allows users to add a review for a restaurant. It validates the input, checks for inappropriate content, and updates the database.
```.py
def add_review(self):
    # I retrieve the dish, rating, and comment entered by the user from the UI.
    dish = self.ids.dish_spinner.text
    rating = self.ids.rating_input.text
    comment = self.ids.comment_input.text

    # I check if any of the fields are empty.
    if not dish or not rating or not comment:
        # If any field is empty, I show an error message and return.
        self.show_error("Please fill in all fields.")
        return

    try:
        # I convert the rating to a float and validate that it is between 1 and 5.
        rating = float(rating)
        if rating < 1 or rating > 5:
            # If the rating is invalid, I show an error message and return.
            self.show_error("Rating must be between 1 and 5.")
            return
    except ValueError:
        # If the rating is not a number, I show an error message and return.
        self.show_error("Rating must be a number.")
        return

    # I check if the comment contains inappropriate content.
    flagged_reason = self.check_for_inappropriate_content(comment)
    if flagged_reason:
        # If the comment is flagged, I show an error message and send the review for moderation.
        self.show_error(
            f"Your message was flagged as inappropriate and was sent for review. Reason: {flagged_reason}. TasteTogether is a platform for collaboration, sharing experiences, and improving the food industry. Help us keep our safe space!")
        self.send_for_review(dish, rating, comment, flagged_reason)
        return

    # I open a connection to the SQLite database using the DatabaseManager class.
    db = DatabaseManager('project.sql')

    # I retrieve the current user's ID from the LoginScreen class.
    user_id = LoginScreen.current_user
    if not user_id:
        # If the user ID is not found, I show an error message and return.
        db.close()
        self.show_error("User not found. Please log in again.")
        return

    # I insert the new review into the reviews table.
    query = "INSERT INTO reviews (restaurant_id, user_id, dish, rating, comment) VALUES (?, ?, ?, ?, ?)"
    db.execute(query, (self.restaurant_id, user_id, dish, rating, comment))

    # I update the restaurant's rating in the database.
    self.update_restaurant_rating(self.restaurant_id, rating)

    # I close the database connection.
    db.close()

    # I clear the input fields to prepare for the next review.
    self.ids.dish_spinner.text = "Select Dish"
    self.ids.rating_input.text = ""
    self.ids.comment_input.text = ""

    # I reload the reviews to reflect the new addition.
    self.load_restaurant(self.restaurant_id)
```

### How It Works - Summary
1. Input Validation: The function checks if all fields are filled and validates the rating.

2. Inappropriate Content Check: It checks if the comment contains inappropriate content and flags it if necessary.

3. Database Insertion: It inserts the new review into the database and updates the restaurant's rating.

4. Error Handling: It shows appropriate error messages for invalid inputs or database errors.

5. UI Update: It clears the input fields and reloads the reviews to reflect the new addition.

## Load Flagged Reviews Function
This function loads flagged reviews from the database and displays them in the UI for moderators to review. Moderators can either approve or reject flagged reviews.
```.py
def load_flagged_reviews(self):
    # I open a connection to the SQLite database using the DatabaseManager class.
    db = DatabaseManager('project.sql')

    # I define a SQL query to fetch all flagged reviews along with the username of the user who posted the review.
    query = """
    SELECT f.id, f.dish, f.rating, f.comment, f.reason, u.username 
    FROM flagged_reviews f 
    JOIN users u ON f.user_id = u.id
    """
    # I execute the query and store the results in the `flagged_reviews` variable.
    flagged_reviews = db.search(query)

    # I close the database connection to free up resources.
    db.close()

    # I clear the existing flagged reviews from the UI to prepare for displaying the new ones.
    self.ids.flagged_reviews.clear_widgets()

    # I iterate over each flagged review to create a UI element for it.
    for review in flagged_reviews:
        # I unpack the review details from the tuple.
        review_id, dish, rating, comment, reason, username = review

        # I create a vertical BoxLayout to hold the review details.
        review_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)

        # I create a Label widget to display the review details.
        review_box.add_widget(Label(
            text=f"User: {username}\nDish: {dish}\nRating: {rating}\nComment: {comment}\nReason: {reason}",
            color=(0, 0, 0, 1),  # Black color
            halign='left'  # Align text to the left
        ))

        # I create an "Approve" button to allow moderators to approve the review.
        approve_btn = Button(
            text="Approve",
            size_hint_y=None,
            height=30,
            on_release=lambda btn, rid=review_id: self.approve_review(rid)
        )

        # I create a "Reject" button to allow moderators to reject the review.
        reject_btn = Button(
            text="Reject",
            size_hint_y=None,
            height=30,
            on_release=lambda btn, rid=review_id: self.reject_review(rid)
        )

        # I add the "Approve" and "Reject" buttons to the review_box.
        review_box.add_widget(approve_btn)
        review_box.add_widget(reject_btn)

        # I add the review_box to the flagged_reviews widget to display it on the screen.
        self.ids.flagged_reviews.add_widget(review_box)
```

### How It Works
1. Data Retrieval: The function queries the database to fetch all flagged reviews along with the username of the user who posted the review.

2. UI Clearing: It clears the existing flagged reviews from the UI to prepare for displaying the new ones.

3. UI Rendering: For each flagged review, it creates a BoxLayout to display the review details and adds "Approve" and "Reject" buttons.

4. Button Actions: The buttons are linked to functions that handle the approval or rejection of the review.

5. Resource Management: The database connection is closed after fetching the data.

## Approve Review Function
```.py
def approve_review(self, review_id):
    # I open a connection to the SQLite database using the DatabaseManager class.
    db = DatabaseManager('project.sql')

    try:
        # I fetch the restaurant_id associated with the flagged review.
        restaurant_id = db.search("SELECT restaurant_id FROM flagged_reviews WHERE id = ?", (review_id,))[0][0]

        # I fetch the details of the flagged review.
        flagged_review = db.search("SELECT user_id, dish, rating, comment FROM flagged_reviews WHERE id = ?", (review_id,))[0]

        # I move the approved review to the general reviews table.
        db.execute("INSERT INTO reviews (restaurant_id, user_id, dish, rating, comment) VALUES (?, ?, ?, ?, ?)",
                   (restaurant_id, flagged_review[0], flagged_review[1], flagged_review[2], flagged_review[3]))

        # I delete the review from the flagged_reviews table.
        db.execute("DELETE FROM flagged_reviews WHERE id = ?", (review_id,))

        # I commit the changes to the database.
        db.commit()
    except Exception as e:
        # If an error occurs, I print the error message.
        print(f"Error approving review: {e}")
    finally:
        # I ensure the database connection is closed, even if an error occurs.
        db.close()

    # I reload the flagged reviews to reflect the changes.
    self.load_flagged_reviews()
```
### How It Works - Summary
1. Data Retrieval: The function fetches the restaurant ID and review details from the flagged_reviews table.

2. Review Approval: It inserts the review into the reviews table and deletes it from the flagged_reviews table.

3. Error Handling: If an error occurs, it prints the error message.

4. Resource Management: The database connection is closed in the finally block.

5. UI Update: The flagged reviews are reloaded to reflect the changes.

## References (Criteria C)
- (https://uxwing.com/star-half-icon/)
- (https://thenounproject.com/icon/full-star-687429/)
- (https://www.flaticon.com/free-icon/empty-star_13595)
- ChatGPT for generating sample data and information
-   [Kivy Crash Course by Tech With Tim](https://www.youtube.com/watch?v=l8Imtec4ReQ)  
-  [KivyMD Tutorial by Code With Stein](https://www.youtube.com/watch?v=ZQ8w1Vb0J6g)  
-  [KivyMD Official Documentation](https://kivymd.readthedocs.io/en/latest/)  
- [Kivy Popup Tutorial by CodersLegacy](https://coderslegacy.com/python/kivy-popup/)  
-  [Real Python - Kivy Guide](https://realpython.com/mobile-app-kivy-python/)  
- [Kivy Discord](https://discord.gg/kivy)  
- [r/Kivy Subreddit](https://www.reddit.com/r/kivy/)  

# Criteria D
[VIDEO](https://drive.google.com/file/d/1FKDrEmS9MIMzgFyiMJR-zSRNpPpdlbhS/view?usp=sharing)

## Appendix
Evidence of Consultation with Client:

![image](https://github.com/user-attachments/assets/f2383c4f-99c1-4078-92ec-1bfda717c592)

Fig. 16, Evidence of Confirmation of Success Criteria

![Screenshot 2025-03-11 005110](https://github.com/user-attachments/assets/57aec91a-5865-4cde-ad05-7be885a57c4c)

Fig. 17, email to the client

![Screenshot 2025-03-11 004911](https://github.com/user-attachments/assets/17fd3da9-480e-4575-81ad-a20f672749e2)

Fig. 18, email from the client with approval



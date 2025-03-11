# Criterion A
## Problem definition

Ms U, a food influencer, relies on honest and high-quality reviews to guide her audience. She is frustrated by unreliable ratings, fake reviews, and a lack of personalization in current food critique platforms. Many platforms allow users to rate restaurants without proof of visit, making it easy for trolls, bots, and competitors to manipulate ratings, ultimately reducing credibility. Additionally, current food rating platforms fail to consider individual taste preferences when recommending restaurants or dishes, leading to irrelevant suggestions that do not align with a user's culinary interests. On top of that, limited sorting options prevent users from filtering restaurants based on specific needs such as price range, culinary interests, popularity, or dietary restrictions, restricting their ability to find the best dining experiences efficiently. Another major issue is that users who take the time to write detailed and thoughtful reviews receive little to no recognition, discouraging engagement and lowering the overall quality of contributions.

As a food influencer, Ms. U frequently collaborates with restaurants and producers, gaining insight into their operational challenges. Restaurants rely on customer feedback to refine their offerings, yet they often struggle to extract meaningful insights from unstructured or misleading reviews. Without a way to engage with credible critiques, they face difficulty in addressing genuine concerns while filtering out bad-faith criticism. Meanwhile, food producers play a crucial role in maintaining quality and sustainability in the industry, but their lack of involvement in existing review ecosystems makes it hard for them to adapt to restaurant demands. Ms. U sees how these gaps in communication and credibility negatively impact both businesses and consumers, reinforcing the need for a more interconnected and transparent system that benefits the entire food industry.

(See evidence of Consultation in Appendix)

## Proposed solution

I chose to develop a desktop application over a website for its stability, performance, and security. Unlike web applications, which require constant internet connectivity and can suffer from network latency, and depends on a server, a desktop app processes data locally, handles large datasets, reducing wait times and improving user experience [[1]](https://www.ifourtechnolab.com/blog/web-app-vs-desktop-app#:~:text=Desktop%20apps%20usually%20offer%20better,you%20prioritize%20speed%20or%20convenience.) [[2]](https://builtbright.io/en/magazine/web-vs-desktop-applications-pros-and-cons/). It also provides enhanced security by enforcing stricter access controls and local encryption, avoiding vulnerabilities like cross-site scripting and SQL injection [[3]](https://www.softwareseni.com/identifying-and-assessing-risks-in-web-and-app-development/) [[4]](https://rubygarage.org/blog/risk-management-in-development).

I chose Python for GUI development due to its readability and cross platform compatibility, making understanding and future modifications easier for stakeholders [[5]](https://serokell.io/blog/python-pros-and-cons) [[6]](https://www.geeksforgeeks.org/python-language-advantages-applications/). It is also lightweight compared to lower-level languages like C++ and Java, ensuring efficiency without unnecessary complexity [[7]](https://www.snaplogic.com/glossary/python-vs-java-performance) [[8]](https://lset.uk/blog/unveiling-the-future-of-python-exploring-the-latest-trends-and-innovations-in-2023-and-beyond/) [[9]](https://blog.jetbrains.com/pycharm/2023/10/future-of-data-science/). 

I chose KivyMD because it provides a modern, visually appealing, and user-friendly interface based on Google’s Material Design [[10]](https://kivymd.readthedocs.io/en/latest/) [[11]](https://m2.material.io/design/introduction/). It ensures a smooth and consistent experience across devices, making navigation intuitive and interactions seamless. Unlike **Tkinter**, which has a basic and outdated appearance, KivyMD offers a polished and engaging design that enhances usability[[11]](https://kivy.org/#home) [[12]](https://medium.com/@qasim.coder/python-gui-smackdown-unleashing-the-power-of-tkinter-pyqt-and-kivy-e7b05d0e862).

I chose SQLite for data storage because it is lightweight, serverless, and cost-effective while efficiently handling structured data like user reviews and restaurant details [[13]](https://www.sqlite.org/whentouse.html) [[14]](https://www.epicweb.dev/why-you-should-probably-be-using-sqlite) [[15]](https://www.sqlite.org/aff_short.html). Unlike **MySQL** or **PostgreSQL**, which require a dedicated server and maintenance, SQLite operates locally with minimal setup, making it ideal for a fast and seamless user experience [[16]](https://www.greengeeks.com/blog/sqlite-vs-mysql/#:~:text=Ultimately%2C%20SQLite%20is%20a%20lightweight,go%2Dto%20for%20RDBMS%20solutions.).

## Success criteria
[success criteria (2).pdf](https://github.com/user-attachments/files/19197099/success.criteria.2.pdf)

**EVIDENCE OF APPROVAL
**
(Also included in Appendix)

![Screenshot 2025-03-11 005110](https://github.com/user-attachments/assets/c7657994-372c-42a0-bc80-05d5938cf052)

Fig. 1, email to the client

![Screenshot 2025-03-11 004911](https://github.com/user-attachments/assets/0eb28cb8-bd64-4a2c-b12c-f990edafd543)

Fig. 2, email from the client with approval

# Criterion B
## Systems Diagram
![systemdiagramp3](https://github.com/user-attachments/assets/8d04a37c-fdb2-499a-8d6e-a81207d536f9)

Fig. 3, solution's hardware and software components and interactions

## Wireframe diagram

## UML Diagram

## ER Diagram

## Flow Diagrams





## Data Storage
Tables in my SQL file

![image](https://github.com/user-attachments/assets/f0731882-50ea-4bf9-8e53-532d343266fe)

Fig. , 10 tables in database (2 default)

Extract from one of the tables

![image](https://github.com/user-attachments/assets/30ed05a6-ceb2-48a9-93c6-4bfd5aa87445)

Fig. , extract showing an example of how data is stored

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
| 2. Personalization | The platform will predict whether a user will enjoy a dish based on their taste profile and past reviews, improving recommendation accuracy and ensuring that feedback is relevant to the user’s preferences. | 1. Run project.py 2. Find and check the terms and conditions box. 3. Find and click LOG IN button. 4. Find and click respective text boxes to enter the folllowing information (past reviews and taste profile is needed for recommendation) Username: 1, Password: 12345678 5. Find and click LOG IN button 6. Find and click DropDown filters next to the search bar on the top of the screen. 7. Select rating 8. See restaurants and ranking 9. Find and click Dropdown filters again 10. Select recommended 11. See difference in restaurants and ranking. | Ranking based on user's previous reviews and taste profile from those reviews.|
| 3. Moderation | An automated system with a blacklist will flag inappropriate reviews containing offensive language, spam, or misleading content, for the moderators to review and delete if necessary. | 1. Complete steps 1-9 from test 1 or 1-4 from test 2 (Username: Bob, Password: 12345678) if steps 1-9 from test 1 have already been tested 2. Find and select view details button of any restaurant (eg. Burger King). 3. Find and click dropdown dishes, select any (eg. Whopper) 4. Click on Rating text box, type a rating (eg. 2). 5. Click on Comment text box, type an inappropriate comment including swear words (eg. "Tastes like shit"). 6. Find and click Submit Review button. 7. Read Pop up dialogue. 8. Find and click back arrow button. 9. Find and click logout button. 10. Click on username text box and type "mod1" 11. Click on password text box and type "12345678". 12. Find and click LOG IN button. 13. Scroll down screen. 14. Find newly flagged review at the bottom. 15. Find and click delete button. | Review is not published, flagged, and sent to moderators for review. Moderator can view the flagged review and approve or delete it. |
| 4. Review Management | Users can leave reviews for restaurants including dish name, rating, and comment. Restaurant owners can view categorized reviews for their restaurant. | 1. Complete steps 1-3 from test 3. 4. Click on Rating text box, type a rating (eg. 5). 5. Click on comment text box, type a comment (eg. "I really enjoyed the meal and atmosphere"). 6. Find and click Submit Review button. 7. Scroll down in Reviews box, and find newly added review. 8. Complete steps 8-9 from test 3. 10. Click on username text box and type "BurgerKing"



# Criterion C


## Appendix
Evidence of Consultation with Client:

![image](https://github.com/user-attachments/assets/f2383c4f-99c1-4078-92ec-1bfda717c592)
Evidence of Confirmation of Success Criteria

![Screenshot 2025-03-11 005110](https://github.com/user-attachments/assets/57aec91a-5865-4cde-ad05-7be885a57c4c)

![Screenshot 2025-03-11 004911](https://github.com/user-attachments/assets/17fd3da9-480e-4575-81ad-a20f672749e2)


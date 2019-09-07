<h1>eDress - clothes exchange website</h1>
eDress is an online platform for exchanging your clothes with other members. 
If you are bored of your wardrobe and want some new catchy pieces but can't afford it, here you can change your clothes with somebody else for free.
<br>This website was made as a project for Code Institute.
<br>To view the live site press <a href="https://edress-project.herokuapp.com/">HERE</a>
<h2>How Does It Work?</h2>
It's as simple as you uploading the information and images of your clothes and then when you have something to show you go roam the dashboard of the clothes already there from other users. When you find something you like, you communicate with them if they would like anything from your collection and if yes, then you exchange addresses and send the piece of clothing for each other. It's as simple as that!
<h2>Idea and goals of the website</h2>
eDress is a website born from an idea of saving money as well as Earth, reusing and reducing the influence of huge brands and corporations using second-world countries and their people for their benefit without giving them equal right. More about the ideas eDress is based on you can find by watching a movie <a href="https://truecostmovie.com/">"True Cost"</a>

<h2>UX</h2>
The website was made for people who want to change their fashion fast but don't want to buy so many new clothes or go to the stores. Also for somebody who wants to save some money and be a part of recycling.<br><br>
These user stories were made during planning stage and were used in creating different features for the website:<br>
<ul>
<li>As a woman, I have a lot of clothes I don't use and would love to change them into something interesting instead of just throwing them out or bringing them to charity.</li>
<li>As a teenager, I am interested in having new clothes to go with fashion but don't have enough space in my closet so, I'd like to exchange them to new ones.</li>
<li>As a starting dizainer, I like to experiment with clothes to make them interesting but it can get expensive quickly so I'd prefer exchanging my made clothes for new ones and getting some feedback.</li>
<li>As a minimalist, I'd like to gift my clothes to both free some space and save on money by exchanging them to other clothes instead of buying new ones.</li>
</ul>
Also, in the planning stage, I created <a href="{{url_for('static', filename='wireframes/wireframes.pdf')}}">these</a> wireframes. Although, the design and some features changed over the development process.

<h2>Features</h2>
<ul>
<li>Home page with displayed available clothes</li>
<li>Edit and Delete Clothes functionalit</li>
<li>Each piece page with info about it</li>
<li>About page for the website</li>
<li>Add New Clothes functionality</li>
<li>Pagination for the home page</li>
</ul>

<h3>Features Left to Implement</h3>
<ul>
<li>Login and register functionality</li>
<li>My Profile page with favourite clothes list</li>
<li>Messaging functionality between the users</li>
<li>'I want this' button to notify the user if someone wants to do an exchange</li>
<li>Reviews & ratings</li>
<li>Male/ female/ kids/ universal categories.</li>
</ul>
<h2>Technologies Used</h2>
<ul>
<li><strong><a href="https://www.w3schools.com/html/html5_intro.asp">HTML5</a></strong>- used to build the main structure and text of the page;</li>
<li><strong><a href="http://www.css3.info/">CSS3</a></strong>- used for the styling of the page;</li>
<li><strong><a href="https://www.javascript.com/">JavaScript</a> and <a href="https://jquery.com/">jQuery</a></strong> - used for filtering;</li>
<li><strong><a href="https://www.python.org/">Python3</a></strong> - used for all functionality - CRUD</li>
<li><strong><a href="https://www.mongodb.com/">MongoDB</a></strong>- for storing the clothes and users information</li>
<li><strong><a href="https://www.heroku.com/">Heroku</a></strong>- for deploying the page</li>
<li><strong><a href="https://getbootstrap.com/">Bootstrap 4</a></strong>- used for styling and layout of the page.</li>
<li><strong><a href="https://bootswatch.com/minty/">Bootswatch Minty</a></strong>- used as a theme for the page, also card boxes, navigation and form styling;</li>
<li><strong><a href="https://fonts.google.com/">Google Fonts</a></strong>- font 'Poppins' used as the main font of the page;</li>
<li><strong><a href="https://fontawesome.com/">FontAwesome</a></strong>- for icons;</li>
</ul>

<h2>CRUD</h2>
<ul>
<li><strong>Create</strong>- 'Add Clothes' form where you add your pieces to the database</li>
<li><strong>Read (Retrieve)</strong>- get the clothes diplayed in the home page from the database</li>
<li><strong>Update</strong>- you can update each piece of clothing in the database by pressing the 'edit' button</li>
<li><strong>Delete</strong>- you can delete each piece from the database by pressing the 'delete' button</li>
</ul>

<h2>Testing</h2>
<h4>Manual testing:</h4>
<h4>Validating:</h4>
<ul>
<li>HTML and CSS validated using Nu Checker;</li>
<li>JavaScript code validated with JS Lint;</li>
</ul>
<h4>Site responsiveness was tested on these browsers:</h4>
<ul>
<li>Google Chrome</li>
<li>Internet Explorer</li>
<li>Mozilla Firefox</li>
<li>Opera Browser</li>
<li>Microsoft Edge</li>
<li>Safari</li>
</ul>
<h2>Known bugs:</h2>
<ul>
<li>Dropdown list for filters dissapears only if you choose or press on the button again. It does not disspear by pressing outside of the list</li>
<li>You can choose only one of the filters. You cannot filter by all of them</li>
</ul>

<h2>Deployment</h2>
The website was started in the c9 environment and later on transfered and finished in AWS Cloud9. All bigger changes were pushed to the staging area and later on pushed to GitHub and Heroku sites.<br>
Heroku was used to host this project. The following method has been used to achieve a good deployment:
<ol>
<li>Set up the initial app</li>
<li>Link the local Git repository to Heroku.</li>
<li>Create a requirements.txt file, which contains a list of the project dependencies</li>
<li>Create a Procfile, the file that tells Heroku how to run the project.</li>
<li>Logged into Heroku and pushed the files using <i>git push heroku master</i></li>
<li>Added the config variables to Heroku in the settings option</li>
</ol>

<h2>Credits</h2>
<strong>Content</strong><br>
All custom written
<br><br><strong>Pictures</strong><br>
Advanced search on Google copyright free<br>
Photo in the About page - by Shanna Camilleri on <a href="https://unsplash.com/">Unsplash</a>
<br><br><strong>Help from tutorials:</strong><br>
<ul>
<li><a href="https://pythonspot.com/login-authentication-with-flask/">Python Tutorials</a></li>
<li><a href="https://www.youtube.com/watch?v=vVx1737auSE">Pretty Printed on Youtube</a></li>
<li><a href='https://stackoverflow.com/users/520857/populus'>Populus from Stackoverflow - help with pagination</a></li>
</ul>
<strong>Tab icon</strong><br>
Made by <a href"www.flaticon.com">Freepik</a>

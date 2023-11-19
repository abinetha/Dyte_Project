[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2sZOX9xt)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

**Log Data Retrieval** is a comprehensive web-based application designed to simplify the retrieval and analysis of log data. The project includes features for searching, filtering, and visualizing log entries, making it an invaluable tool for managing large sets of log data.

**Key Features:**

**Search Functionality:** Easily search for log entries based on various criteria such as level, message, timestamp, resource ID, and more.

**Date Range Filtering:** Retrieve log entries within a specific date range to focus on relevant data.

**Flexible Search Fields:** Choose from a variety of search fields, including level, message, resource ID, timestamp, trace ID, span ID, commit, and parent resource ID.

**JSON Parsing and Database Storage:** Efficiently parse JSON files, store the log data in a MySQL database, and enable seamless retrieval.

**Visualize Data:** View log data in a structured tabular format on the website, providing a user-friendly interface for analysis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Video Demo

https://github.com/abinetha/Dyte_Project/assets/98078409/d4006e22-cdef-4435-b32c-bf4eaf16964a



### Built With

* Django
* HTML & CSS
* Javascript
* Python
* MySQL

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The Log Ingestor is a component of this project responsible for collecting and storing log entries. It allows you to search and filter logs based on various criteria.

### Prerequisites

Make sure you have the following installed:

- Python (Version 3.10 or above)
- Django
- MySQL (Version 8.0 or above)

### Installation

**Clone the repository:**

git clone https://github.com/abinetha/Dyte_Project.git

**Navigate to the project directory:**

```bash
cd your-repo
```
**Create a virtual environment:**
```bash
python -m venv venv
```
**Activate the virtual environment:**

**On Windows:**
```bash
.\venv\Scripts\activate
```
**On macOS/Linux:**
```bash
source venv/bin/activate
```
**Install dependencies:**
```bash
pip install -r requirements.txt
```
**Run migrations:**
```bash
python manage.py migrate
```
**Create a superuser:**
```bash
python manage.py createsuperuser
```
**Start the development server:**
```bash
python manage.py runserver
```
The project should now be running locally. Access the admin panel at http://127.0.0.1:3000/admin/ and log in with the superuser credentials.


<!-- USAGE EXAMPLES -->
## Usage

**1. Viewing Logs**

**Description:** The Log Viewer allows you to easily view logs through a web-based interface.

**Steps:**
1. Open your web browser and navigate to the Log Viewer website ([http://localhost:3000/](url)).
2. The main page displays log entries in a tabular format.
3. Logs are automatically loaded from the database and updated periodically.

**2. Searching Logs**

**Description:** Use the search functionality to filter logs based on specific criteria.

**Steps:**
1. On the main page, locate the search form.
2. Choose a search field from the dropdown menu (e.g., Level, Message, Timestamp).
3. Enter the search text in the designated input field.
4. Optionally, specify a start and end date for a date range search.
5. Click the "Search" button.
6. The table will update to display logs that match the specified criteria.

**3. Adding Logs**

**Description:** Use the `/save_json_data/` endpoint to add logs to the system.

**Steps:**
1. Make a POST request to [http://localhost:3000/save_json_data/](http://localhost:3000/save_json_data/) with your JSON log data.
2. The system will respond with a success message if the data is saved successfully.
3. If a duplicate entry is detected, a message indicating the duplication will be returned.
4. In case of an error, an appropriate error message will be provided.

**Example using cURL:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"level": "info", "message": "Log entry content", "timestamp": "2023-11-18T12:00:00Z"}' http://localhost:3000/save_json_data/
```

**4. Examples**

**Filter Logs:**

To view all logs, simply navigate to the main page of the Log Viewer.
Searching for Errors:

Select "Level" from the "Search Field" dropdown.
Enter "error" in the "Search Text" input.
Click "Search" to see logs with the "error" level.

**Date Range Search:**

Enter a start date and end date in the respective input fields.
Click "Search" to see logs within the specified date range.



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
If you encounter issues, have suggestions, or would like to contribute to the project, feel free to open issues, submit pull requests, or provide feedback.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Django](https://docs.djangoproject.com/en/4.2/)
* [Python](https://docs.python.org/3/tutorial/index.html)
* [MySQL](https://dev.mysql.com/doc/refman/8.2/en/tutorial.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

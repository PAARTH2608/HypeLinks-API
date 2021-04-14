# Smart Bookmark API
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
<!--   <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">SMART BOOKMARK API</h3>

  <p align="center">
    An API that can classify websites into 10 different categories
    <br />
    <a href="https://github.com/iamyajat/smart-bookmark-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/iamyajat/smart-bookmark-api">Demo (Coming Soon)</a>
    ·
    <a href="https://github.com/iamyajat/smart-bookmark-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/iamyajat/smart-bookmark-api/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

An API that can classify a given url into various different categories.

#### Categories
- Sports
- News
- Fitness & Wellbeing
- Food and Recipes
- Politics
- Entertainment
- Business
- Blogs
- Science & Technology
- NSFW


### Built With

* [Python 3.8.9](https://www.python.org/downloads/release/python-389/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [TensorFlow 2](https://www.tensorflow.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
Python 3.8.9 and the latest version of pip.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iamyajat/smart-bookmark-api.git
   ```
2. Install `virtualenv`
   ```sh
   pip install virtualenv
   ```
3. Create a virtual environment
   ```sh
   python -m venv env
   ```
   ```sh
   env/bin/activate
   ```
4. Install all requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Start the API
   ```sh
   uvicorn main:app --reload
   ```

<!-- USAGE EXAMPLES -->
## Usage

To try the API out, go to [https://127.0.0.1/docs#/](https://127.0.0.1/docs#/) and test the different end-points out.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/iamyajat/smart-bookmark-api/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: AmazingFeature'`) (Please refer to the commit guidelines mentioned [here](https://www.conventionalcommits.org/en/v1.0.0/))
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Yajat Malhotra - [@iamyajat](https://twitter.com/iamyajat)

Project Link: [https://github.com/iamyajat/smart-bookmark-api](https://github.com/iamyajat/smart-bookmark-api)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/iamyajat/smart-bookmark-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/iamyajat/smart-bookmark-api/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/iamyajat/smart-bookmark-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/iamyajat/smart-bookmark-api/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/iamyajat/smart-bookmark-api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/iamyajat
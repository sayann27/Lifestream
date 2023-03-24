<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>LifeStream</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <style>

    </style>

</head>


<body>
    <!-- Navbar -->
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="home.html">
                    <img src="Main logo.png" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
                    LifeStream
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="home.html">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="about.php">About us</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                Venues
                            </a>
                            <ul class="dropdown-menu" data-bs-theme="dark">
                                <!--Enter the section Id for navigating to the specific venue-->
                                <li><a class="dropdown-item" href="venues.php">Bangalore</a></li>
                                <li><a class="dropdown-item" href="venues.php">Delhi</a></li>
                                <li><a class="dropdown-item" href="venues.php">Mumbai</a></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link disabled">Disabled</a>
                        </li>
                    </ul>
                    <button class="btn btn-outline-success" type="submit" onclick= "location.href='login.html'">Login</button>
                </div>
            </div>
        </nav>
    </header>

    <div class="p-5 mb-4 bg-light rounded-3">
        <div class="container-fluid py-5">
            <h1 class="display-5 fw-bold">About Lifestream</h1>
            <p class="col-md-8 fs-4">
                LifeStream is a blood donation management system.
                <br>
                Blood donation is a vital part of worldwide healthcare. <br>
            <ul>
                <li class = "fs-4">
                    It relates to blood transfusion as a life-sustaining and life-saving procedure as well as a form of
                    therapeutic phlebotomy as a primary medical intervention.
                </li>
                <li class = "fs-4">
                    Over one hundred million units of blood are donated each year throughout the world.
                </li>
                <li class = "fs-4">

                    This site makes the process of blood donation seamless and also helps the receivers find blood in
                    cases of emergency quickly.
                </li>
            </ul>



            </p>

        </div>
    </div>



    <!-- About the developers -->
    <footer>
        <p class="h1 text-center my-5">About the developers</p>
        <div class="container text-center">
            <div class="row align-items-start">
                <div class="col">
                    <div class="card" style="width: 18rem;">
                        <!-- 337x337 images -->
                        <img src="profes_photo.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Sayan Mandal</h5>
                            <p class="card-text"> One of the developers of the site Lifestream</p>
                            <a href="https://www.linkedin.com/in/sayan-mandal-394810217/" class="btn btn-primary" target="_blank">Go to LinkedIn</a>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card" style="width: 18rem;">
                        <img src="..." class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Abishek Immanuel</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk
                                of the card's
                                content.</p>
                            <a href="#" class="btn btn-primary" target="_blank">Go to LinkedIn</a>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card" style="width: 18rem;">
                        <img src="..." class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Sneha Varshini</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk
                                of the card's
                                content.</p>
                            <a href="#" class="btn btn-primary" target="_blank">Go to LinkedIn</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
        crossorigin="anonymous"></script>
</body>

</html>
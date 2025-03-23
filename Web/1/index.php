<!DOCTYPE html>
<html>
<head>
    <title>Breaking Bank - Solo Leveling Edition</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <style>
        body {
            background: url('solo_leveling_bg.jpg') no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
        }
        .login-container {
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 20px;
            border-radius: 10px;
            width: 300px;
            text-align: center;
            margin: 100px auto;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 8px;
            margin: 5px 0;
            border-radius: 5px;
            border: none;
        }
        input[type="submit"] {
            background: orange;
            color: black;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Welcome to Breaking Bank</h1>
        <p>Can you bypass the authentication and access the admin panel?</p>
        <form action="login.php" method="POST">
            <label>Username:</label>
            <input type="text" name="username" required><br>
            <label>Password (MD5 Hash Expected):</label>
            <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>

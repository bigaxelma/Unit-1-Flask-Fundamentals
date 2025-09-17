from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <h1>Dynamic Routes Demo<h1>
    <h2>Try these Urls<h2>
<ul>
    <li><a href="/user/john">User profile: John</a></li>
    <li><a href="/user/alice">User Profile: Alice</a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>


"""

@app.route('/user/<username>', methods=['GET'])
def user_profile(username):
    return f'''
     <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile Type: {type(username).__name__}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
    <a href="/"> Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bpb</a>
 </nav>
'''
@app.route("/calc/<int:num1>/<operation>/<int:num2>", methods=['GET'])
def calculator(num1, operation, num2):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else 'Error: Division by zero!'
    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"
    else:
        return f"Unknown operations!{operation}"

@app.route("/temp/<type>/<int:num>", methods=['GET'])
def tempconvert(type, num):
    if (type.lower() == 'f'):
        return f"{num} °F = {(5/9)*(num-32)} °C"
    elif (type.lower() == 'c'):
        return f"{num} °C = {((9/5)*num)+32} °F"
    else:
        return f"Unknown type! {type}"


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
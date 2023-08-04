# Conceptual Exercise

## Questions and Answers

1. **What are the important differences between Python and JavaScript?**

    - Python: Primarily used for backend development, AI, and data analysis.
    - JavaScript: Primarily used for client-side web development but can also be used for backend development via Node.js.

2. **Given a dictionary like `{"a": 1, "b": 2}`, list two ways you can attempt to access a missing key (like "c") without causing your program to crash.**

    - Option 1: Use the 'get' method: `dict.get(key, default)`. This returns the value for the key if it exists, otherwise it returns the default value. If no default value is provided, it returns `None`.
    - Option 2: Use a 'try/except' block. For example:
    /// python
      try:
          value = d['c']
      except KeyError:
          value = 'default
    ///

3. **What is a unit test?**

    A unit test is a type of software testing where individual units of software, often a function or method in OOP, are tested.

4. **What is an integration test?**

    Integration testing is a type of testing to check if different pieces of modules or services work together.

5. **What is the role of a web application framework, like Flask?**

    Frameworks like Flask are designed to streamline the development process, making it more efficient. They provide features such as URL routing, session management, and cookie handling, allowing developers to focus on application logic instead of these low-level details.

6. **How do you choose between passing information to Flask as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel')?**

    - Route parameters are primarily used to identify a specific resource or group of resources.
    - Query parameters are often used to sort/filter resources or return different attributes.

7. **How do you collect data from a URL placeholder parameter using Flask?**

    Data from a URL placeholder can be collected by defining the parameter in the route decorator and including it as an argument to your view function.

8. **How do you collect data from the query string using Flask?**

    Flask's 'request' object can be used to retrieve data from a query string.

9. **How do you collect data from the body of the request using Flask?**

    Data from the body of a request is typically collected during a POST request.

10. **What is a cookie and what is it commonly used for?**

    A cookie is a small piece of data stored on the user's computer by the web browser. Cookies are commonly used to record browsing activity and user preferences. Their extensive tracking capabilities have led to the creation of laws to regulate their use.

11. **What is the session object in Flask?**

    In Flask, a session is a feature that allows the storage of user-specific information from one request to the next. The data is available across all routes and is stored as a cookie. The session data is cryptographically signed to prevent tampering.

12. **What does Flask's `jsonify()` do?**

    The `jsonify()` function in Flask is used to convert Python data structures, like dictionaries and lists, into a JSON format that can be returned as a response in a web application. This is useful when building APIs. `jsonify()` also sets the correct content-type header.

N: Flask’s **request object** stores info about incoming request

#### its useful fields:
* `request.`**`headers`** : HTML headers from client browser
* `request`.**`method`** : GET or POST
* `request`.**`args`** :
  - arguments, as a querystring from GET request
  - immutable dictionary
* `request`.**`form`** :
  - arguments sent via POST request
  - immutable dictionary


---

HTTP request methods

GET:  
• passed through query string
• has size limit (2048chars says IG)
• less secure, since it can be seen in URL
POST:  
• sent in background
• no size limit
• **NOT secure.** just harder to see

---

N: GET is default, but you can specify request type in HTML using a tag attribute.
.  
eg,
```html
<form action="/login" method="GET">
  <input type="text" name="uname">
  <input type="submit" name="login" value="login">
</form>
```
----------
```html
<form action="/login" method="POST">
  <input type="text" name="uname">
  <input type="submit" name="login" value="login">
</form>
```

---

...and specify which requests to handle in Flask:

GET only (use either):
```python
@app.route('/login')
@app.route('/login', methods=["GET"])
```

---

...or POST only:
```python
@app.route('/login', methods=["POST"])
```

---

...or both:
```python
@app.route('/login', methods=["GET","POST"])
```

---

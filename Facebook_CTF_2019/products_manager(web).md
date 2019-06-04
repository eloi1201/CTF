# Question

<img width="498" alt="Screen Shot 2019-06-02 at 10 02 43 PM" src="https://user-images.githubusercontent.com/14992494/58920672-de262800-8765-11e9-9a9a-8e1d1ee85799.png">

# Solution

### add.php
```
function handle_post() {
  global $_POST;

  $name = $_POST["name"];
  $secret = $_POST["secret"];
  $description = $_POST["description"];

  if (isset($name) && $name !== ""
        && isset($secret) && $secret !== ""
        && isset($description) && $description !== "") {
    if (validate_secret($secret) === false) {
      return "Invalid secret, please check requirements";
    }

    $product = get_product($name);
    if ($product !== null) {
      return "Product name already exists, please enter again";
    }

    insert_product($name, hash('sha256', $secret), $description);

    echo "<p>Product has been added</p>";
  }

  return null;
}
```

### db.php
```
/*
CREATE TABLE products (
  name char(64),
  secret char(64),
  description varchar(250)
);

INSERT INTO products VALUES('facebook', sha256(....), 'FLAG_HERE');
INSERT INTO products VALUES('messenger', sha256(....), ....);
INSERT INTO products VALUES('instagram', sha256(....), ....);
INSERT INTO products VALUES('whatsapp', sha256(....), ....);
INSERT INTO products VALUES('oculus-rift', sha256(....), ....);
*/
```

<img width="693" alt="Screen Shot 2019-06-02 at 9 58 48 PM" src="https://user-images.githubusercontent.com/14992494/58920638-bd5dd280-8765-11e9-8724-a140189820ca.png">
<img width="695" alt="Screen Shot 2019-06-02 at 9 59 16 PM" src="https://user-images.githubusercontent.com/14992494/58920641-bdf66900-8765-11e9-832d-b8f4b86a0b29.png">
<img width="694" alt="Screen Shot 2019-06-02 at 10 00 08 PM" src="https://user-images.githubusercontent.com/14992494/58920643-bdf66900-8765-11e9-9815-ce8d318590a9.png">
<img width="691" alt="Screen Shot 2019-06-02 at 10 00 28 PM" src="https://user-images.githubusercontent.com/14992494/58920644-be8eff80-8765-11e9-8599-9fa83ec473f9.png">


# Flag

<img width="689" alt="Screen Shot 2019-06-02 at 10 01 10 PM" src="https://user-images.githubusercontent.com/14992494/58920645-be8eff80-8765-11e9-9256-f8980603dd0c.png">

fb{4774ck1n9_5q1_w17h0u7_1nj3c710n_15_4m421n9_:)}

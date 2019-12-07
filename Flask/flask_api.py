from flask import Flask
app= Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def home():
    return("Hello Flask")


@app.route("/testio",methods=['GET', 'POST'])
def testIO():
    import t1 as t1
    print(t1.ttt())
    #import test_class as tc
    #tc.IO.read("File")
    #print(tc.IO.supportSrcs)
    #print("Test Class Sucess : ",tc.IO.read("File"))

   # return("Hello Test IO !!")

if __name__ == "__main__":
    app.run()

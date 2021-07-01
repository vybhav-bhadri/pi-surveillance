from SmartCamera import creat_app

app=creat_app()

#debug is set false. for development set true
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)



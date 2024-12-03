        cd /root/home/farm/
        git pull
        source venv/bin/activate
        pip install -r requirements.txt
        sudo systemctl restart flaskapp
        systemctl status flaskapp
        systemctl status flaskapp

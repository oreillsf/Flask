# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:Vargheseoreilly123@database2.cwffazstjbiz.eu-west-1.rds.amazonaws.com:3306/practicum'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600


WTF_CSRF_ENABLED = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
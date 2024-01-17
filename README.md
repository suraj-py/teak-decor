
# Teak Decor
Developed a fully functional‬‭ furniture e-commerce‬ ‭website using ‬‭Django ‬‭and utilized ‬‭TailwindCSS ‬‭for front-end‬.

Created a comprehensive ‬‭product catalog ‬‭with‬‭ categories‬‭ for easy navigation.‬

Developed a ‬‭shopping cart system‬‭ that allows users to add, update, and remove items.‬

Integrated the ‬‭Stripe API‬‭ as the ‬‭payment gateway ‬‭for secure and seamless transactions.

Utilized ‬‭AWS S3‬‭ for ‬‭storing‬‭ and ‬‭serving‬‭ media files,‬‭such as product images and Set up‬‭ AWS Cloudflare‬‭as a CDN to ‬‭optimize ‬‭website ‬‭performance and ensure faster content delivery.‬


## Demo
![](demo/teak_decor_demo.gif)

## Run Locally

Create virtual environment

```bash
  pipenv shell
```

Clone the project

```bash
  git clone https://github.com/suraj-py/teak-decor.git
```
Install dependencies

```bash
  pip install -r requirements.txt
```


Create .env file and configure AWS settings

```code
AWS_ACCESS_KEY_ID = 'your aws access key id'
AWS_SECRET_ACCESS_KEY = 'your secret access key'
AWS_STORAGE_BUCKET_NAME = 'your aws s3 bucket name'
AWS_S3_REGION_NAME = 'your aws s3 region name'
```

Now edit this settings.py file

Start the server

```bash
  python manage.py runserver
```

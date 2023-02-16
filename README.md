# easily run pyspark and read from aws


## important stuff
### pyspark

it took really **long** time to figure out this config, ***LEARNINGS:***
* s3a has to be used to access files
* most configs have to be set in the instantiated spark context
* they have to have their `fs.s3X.impl` set
* you need the hadoop in the correct version as pyspark
* `aws-java-sdk-bundle` is also needed
* or manually set the env variables:
  ```ini
  export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
  export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  export AWS_DEFAULT_REGION=us-west-2
  ```
  accordingly
* IF using SSO: `ProfileCredentialsProvider` does not work with sso atm, you need to:
  * use such a script [default credentials](https://gist.github.com/zartstrom/2ead1504f679fdcc1c16e77284ca8126) to insert the above mentioned values into your `.aws/credentials`
  * set the env variable accordingly `export AWS_PROFILE=default`# pyspark_setup

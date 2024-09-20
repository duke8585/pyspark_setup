# easily run pyspark and read from aws


## important stuff

### prerequisites

you will need a java version @8 or @11 according to the [compatibility matrix](https://sparkbyexamples.com/spark/spark-versions-supportability-matrix/) for pyspark. this is most easily done using [sdkman](https://github.com/sdkman/sdkman-cli). after installing - including adding the sourcing of sdkman to e.g. your `.zshrc` - you an simply

```sh
sdk install java 11.0.24-zulu
sdk use java 11.0.24-zulu
```


### installing it

the Makefile has it all. mostly, you will need homebrew and pyenv on your machine. then, you run `make setup`. it may be that you have to restart your shell and add a section to the `.bashrc` or `.zshrc` to properly install pyenv.


### pyspark

you can run the sample dummy df via `python -i main.py` and interactively play in the session with the df object.

#### reading from s3

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
  * full recipe when chaining roles:
    * get credentials for source profile, add them to stanza in `~/.aws/credentials`
    * get credentials for target profile, add them to stanza in `~/.aws/credentials`
    * set AWS_PROFILE to target profile
    * run script


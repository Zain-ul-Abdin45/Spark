# Apache PySpark

- Apache Spark is written in Scala Programming Language.PySpark actually is a Python API for Spark.
- It does in-memory computations to analyze data in real-time with batch-processing.



- Installing PySpark in Windows
- For Installing PySpark you'll need Java Development Kit first.
 
=> Download updated JAVA JDK from https://www.oracle.com/java/technologies/downloads/ according to your requirements.

=> Extract the JDK to C Disk and then add JAVA_PATH to enviroment variables i,e in user variables.

=> Then %JAVA_HOME%\bin to System variables path

=> Download Pyspark from https://www.apache.org/dyn/closer.lua/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz


=> Extract the PySpark to C Disk and then add SPARK_PATH to enviroment variables i,e in user variables.


=> Then %SPARK_HOME%\bin to System variables path

You'll have a ready enviroment You can check by running spark-shell in cmd.
![image](https://user-images.githubusercontent.com/47116254/209581244-9dba3d45-941f-4bf2-810d-798f9cff3272.png)

- Installing PySpark in Ubuntu Environment

=> Check whether the JAVA is already installed by entering javac -version in terminal.

- Installing JDK in Ubunutu Through Terminal
If JAVA is not available Terminal will recommend to install any JDK by mentioning different versions.

=> sudo apt-get update
=> sudo apt install openjdk-8-jdk-headless
=> tar xvzf file.tar.gz -/path/to/yourdirectory

- Adding JDK to Path
=> You can add JDK by entering below commands:
=> export JAVA_HOME=/yourdirectory/openjdk-8-jdk-headless
=> export PATH=$PATH:$JAVA_HOME\bin
Remember no spacing between variables
OR you can edit /.bashrc in terminal 
=> nano ~/.bashrc
add these variables in file and save export JAVA_HOME=/yourdirectory/openjdk-8-jdk-headless
                                     export PATH=$PATH:$JAVA_HOME\bin

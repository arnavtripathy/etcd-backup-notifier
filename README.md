**ETCD Backup Automation**


ETCD data is a crucial part of a kubernetes cluster. As such a regular backup system should be created to make sure that all the data is stored someplace to be used in case of a total cluster failure . This implementation should also address the following issues:-

- Since etcd runs on localhost of the master node , hence our implementation might require scheduling workloads on the master node. So care must be taken that it should not take up too much CPU or memory power .
- It should have a good alerting system. The stakeholders and the administrator should get regular alerts about the backing up.
- The data should be kept in a proper and reliable location so that it can be easily restored in case of emergency.
- Automation is key. The whole process should not require any stakeholder interaction unless there's an absolute necessity

While preparing a solution, we have addressed the issues and come up with a strategy which we have represented in the below diagram:

![alt text](<etcd.PNG>) 




The general flow of the backup process goes something like this:-

- A system cronjob at a particular time in the day schedules a kubernetes job which will create a snapshot of the etcd data and store it in the node host path. This is a containerised process which does not take up  a lot of computation power of the node.
- The data will be automatically pushed to a remote s3 bucket and the job will be deleted. This solves the reliability of the data storage issue.
- An email and slack alert is sent whenever a backup action happens both for success and failure. This is to doubly ensure that things are going fine.
- All of this is completely automated using python and bash. 

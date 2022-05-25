kubectl apply -f /home/ubuntu/job-etcd.yaml
sleep 5
cd /home/ubuntu/backups
fetcd=$(echo ls etc*)

aws s3api put-object --bucket "s3 bucket-name" --key etcd-backups/$($fetcd) --body $($fetcd)

rm  $($fetcd)
kubectl delete job etcd-backup -n kube-system

# Increase nginx to serve more requests

 exec {'increase_worker_connections':
  provider => shell,
  command  => 'sudo sed -i "s/worker_connections 1024;/worker_connections 4096;/" /etc/nginx/nginx.conf',
  before   => Exec['restart_nginx'],
}

exec {'restart_nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}


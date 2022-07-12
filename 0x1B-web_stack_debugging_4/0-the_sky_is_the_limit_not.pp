#using puppet to fix nginx ulimit

exec { 'change ulimitt':
  command => 'sed -i \'s/^ULIMIT=.*/ULIMIT="-n 4096"/g\' /etc/default/nginx',
  path    => '/bin/',
}

-> exec { 'nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
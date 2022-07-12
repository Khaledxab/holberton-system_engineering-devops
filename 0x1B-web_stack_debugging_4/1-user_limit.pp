# using puppet to edit /etc/security limits.conf
# nofile hard+soft limit
exec { 'fix nofile':
  command => 'sed -i \'s/^holberton hard nofile.*/holberton hard nofile 64000/g\' /etc/security/limits.conf',
  path    => '/bin/',
}

exec { 'fix soft limit':
  command => 'sed -i \'s/^holberton soft nofile.*/holberton soft nofile 64000/g\' /etc/security/limits.conf',
  path    => '/bin/',
}
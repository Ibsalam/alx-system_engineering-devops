# Execute a command
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}

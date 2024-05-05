#the configure of ssh config

file_line{'Turn off passwd auth':
   line => 'PasswordAuthentication no'  
   path => '/etc/ssh/ssh_config',
  
}

file_line{'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}

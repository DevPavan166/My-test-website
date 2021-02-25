const options = {
    bottom: '64px', // default: '32px'
    right: 'unset', // default: '32px'
    left: '64px', // default: 'unset'
    time: '0.5s', // default: '0.3s'
    mixColor: '#fff', // default: '#fff'
    backgroundColor: '#fff',  // default: '#fff'
    buttonColorDark: '#100f2c',  // default: '#100f2c'
    buttonColorLight: '#fff', // default: '#fff'
    saveInCookies: true, // default: true,
    label: '🌓', // default: ''
    autoMatchOsTheme: true // default: true
  }
  

const darkmode =  new Dark(options);
darkmode.showWidget();
console.log(darkmode.isActivated()) // will return true

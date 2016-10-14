$(document).ready(function() {
    var lock = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, {
    	languageDictionary: {
    	    title: "IWS"
    	},
		theme: {
			logo: '/static/images/test-icon.png',
			primaryColor: ' blue'
		},
		additionalSignUpFields: [{
		    name: "address",
		    placeholder: "enter your address",
			// The following properties are optional
			validator: function(address) {
				return {
					valid: address.length >= 10,
					hint: "Must have 10 or more chars" // optional
					};
			    }
			 },
			{
				 name: "full_name",
				 placeholder: "Enter your full name"
		}],
		auth: {
	    	redirectUrl: AUTH0_CALLBACK_URL,
	    	responseType: 'code',
	    	params: {
	    		api: true
	    	}
		},
    });
     
    var employee = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, {
		theme: {
			logo: '/static/images/test-icon.png',
			primaryColor: ' blue'
		},
		allowSignUp: false,
		auth: {
	    	redirectUrl: AUTH0_CALLBACK_URL,
	    	responseType: 'code',
	    	params: {
	    		api: true
	    	}
		},
	});

    $('.btn-primary').click(function(e) {
      lock.show();
    });
    
    $('#btn-employee').click(function(e) {
        employee.show();
      });
});
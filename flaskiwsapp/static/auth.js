$(document).ready(function() {
     var lock = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, {
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

    $('.btn-login').click(function(e) {
        console.log(e);
      //e.preventDefault();
      lock.show();
    });
});

<!DOCTYPE html>
<html lang="en">

<head>

	<meta charset="utf-8">

	<title>Subjective tests plateform - {{config["name"]}}</title>

	<!-- Bootstrap Core CSS -->
	<link href="{{APP_PREFIX}}/static/css/bootstrap.min.css" rel="stylesheet">
	<link href="{{APP_PREFIX}}/static/css/tests.css" rel="stylesheet">
	<link href="{{APP_PREFIX}}/static/css/jquery-ui.min.css" rel="stylesheet">
	<link href="{{APP_PREFIX}}/static/css/perceval.css" rel="stylesheet">
	<script src="{{APP_PREFIX}}/static/js/jquery.js"></script>
	<script src="{{APP_PREFIX}}/static/js/jquery-ui.min.js"></script>
	<script src="{{APP_PREFIX}}/static/js/perceval.js"></script>

</head>

<body>

	<div class="container">
		<div class="row">
			<div class="col-md-4 col-md-offset-4 text-center">
			<h1>{{config["name"]}}</h1>
			<p class="lead">{{config["description"]}}</p>
			</div>
		</div>
	</div>

	<div class="jumbotron">
		<div class="container">
			<div class="row">
				<div class="col-md-6 col-md-offset-3">
					<h2 class="text-center">Test terminé !</h2>
					<h2 class="text-center">Merci pour votre temps.</h2>
					<br>
					<br>
					<h4 class="text-center">Vous avez été déconnecté. Vous pouvez fermer la page.</h4>
					<br>
				</div>
			</div>
		</div>
	</div>

	</body>

</html>

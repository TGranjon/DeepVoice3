<!DOCTYPE html>
<html lang="en">

<head>

	<meta charset="utf-8">

	<title>Subjective tests platform - {{config["name"]}}</title>

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
				<div class="col-md-4 col-md-offset-4">
					<h3>Merci de renseigner le jeton qui vous a été donné lors de la création de ce test.</h3>
					<form role="form" action="{{APP_PREFIX}}/export" method="POST">
						<fieldset>
							<div class="form-group">
								<input type="text" class="form-control" placeholder="Token" name="token" autofocus required>
							</div>
							<!-- Change this to a button or input when using this as a form -->
							<input type="submit" value="DB" name="type" class="btn btn-lg btn-success btn-block" value="Export DB">
							<input type="submit" value="CSV" name="type" class="btn btn-lg btn-success btn-block" value="Export CSV">
						</fieldset>
					</form>
					<br>
					%if defined('error') and error != "" :
					<div class="alert alert-danger">
						<p><strong>Error !</strong>  {{error}}</p>
					</div>
					%end
				</div>
			</div>
		</div>
	</div>
</html>

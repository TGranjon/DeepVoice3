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
		<h3>
		Ce test perceptif comporte une page d'introduction afin de prendre en main la plateforme puis 40 pages de test proprement dit.
		Vous pouvez interrompre à tout moment le test et le reprendre en vous reconnectant avec la même adresse mail.
		Les résultats seront validés lorsque vous serez arrivés au bout des 40 étapes.
		<br><br>
		Chaque page contient deux questions : on vous demande d'abord de choisir entre deux signaux celui que vous préférez en terme de qualité et ensuite on vous demande d'écrire les mots que vous avez entendu dans le troisième signal. ATTENTION : les extraits sont généralement différents entre les deux questions.
		<br><br>
		Pour passer à l'étape suivante, il faut avoir écouté les trois extraits et rempli le champ de texte.
		<br><br>
		L'évaluation prend entre 30 et 40 minutes.
		</h3>
	</div>

	<div class="jumbotron">
		<div class="container">
			<div class="row">
				<div class="col-sm-6 col-sm-offset-3 col-md-4 col-md-offset-4">
					<h3>Merci de fournir une adresse mail pour vous identifier:</h3>
					<form role="form" action="{{APP_PREFIX}}/login" method="POST">
						<fieldset>
							<div class="form-group">
								<input type="text" class="form-control input-lg" placeholder="E-mail" name="email" autofocus required>
							</div>
							<!-- Change this to a button or input when using this as a form -->
							<input type="submit" class="btn btn-lg btn-success btn-block" value="Start/Continue">
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

	</body>

</html>

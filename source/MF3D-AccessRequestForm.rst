
.. raw:: html

	<form action="https://api.web3forms.com/submit" method="POST">

		<!-- Replace with your Access Key -->
		<input type="hidden" name="access_key" value="4de23ca9-501d-4491-9a80-3fa912393938">

		<!-- Form Inputs. Each input must have a name="" attribute -->
		<p>
			<label for="name">Name:</label>
			<input type="text" name="name" required>

			<label for="email">E-mail:</label>
			<input type="email" name="email" required>

			<label for="affiliation">Affiliation:</label>
			<input type="text" name="affiliation" required>
		</p>
		<p>
			<label for="message">Brief description of planned data usage:</label>
			<br>
			<textarea name="message" rows="4" cols="75" required></textarea>
		</p>
		<p>
			<label for="agree">I agree to the terms of use under the Creative Commons <i class="fa-brands fa-creative-commons"></i> license:</label>
			<input type="checkbox" name="agree" required>
		</p>

		<!-- Honeypot Spam Protection -->
		<input type="checkbox" name="botcheck" class="hidden" style="display: none;">

		<!-- Custom Confirmation / Success Page -->
		<!-- <input type="hidden" name="redirect" value="https://mywebsite.com/thanks.html"> -->

		<button type="submit">Submit Access Request</button>

	</form>

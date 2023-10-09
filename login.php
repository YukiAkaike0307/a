<?php
session_start();

// ユーザー情報の検証（データベースやファイルから検証）
if (/* ユーザー情報が正しい */) {
  $_SESSION['user'] = /* ユーザー情報 */;
  header('Location: dashboard.php');
} else {
  header('Location: index.html');
}
?>
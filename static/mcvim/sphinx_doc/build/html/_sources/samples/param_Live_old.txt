.. index::
   triple: param; RefreshInterval; refreshOnlySheetMoves

Live où seule la feuille de coup est rafraichie
===============================================

Utilisez |live| pour paser en mode "Full live"

.. code-block:: html

 <applet code="mcvim_chessboard.ChessBoard.class" align="baseline" width="630" height="560">
 <param name="pgngamefile" value="games/live.pgn">
 <param name="refreshInterval" value=1> 
 <param name="refreshOnlySheetMoves" value="on">
 </applet>

.. raw:: html
  
  <applet code="mcvim_chessboard.ChessBoard.class" align="baseline" width="630" height="560">
  <param name="pgngamefile" value="games/live.pgn"/>
  <param name="refreshInterval" value=1> 
  <param name="refreshOnlySheetMoves" value="on">
  </applet>


Voir le `pgn`_ 

.. _`pgn`: games/live.pgn

.. |live| image:: ../switch_live.jpg
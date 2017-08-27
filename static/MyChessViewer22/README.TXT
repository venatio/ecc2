                              MyChessViewer 2.2

This is my Chess PGN applet viewer - hence the name - "MyChessViewer". It plays
over PGN games in your browser. It is meant for website developers that need a
nice viewer and wish to conserve web space/bandwidth.

You may use MyChessViewer freely.  All I ask is that you credit MyChess.com.

Here are some features:

 - Views games in long and short PGN compliant Algebraic notation.
 - Game files can be zipped or uncompressed on the server.  The zip compression
   option will save nicely on disk space and download bandwidth.  The applet
   will detect the zip compression on the fly.
 - Animates moves in an attractive display.
 - Clicking on any move in the score sheet immediatedly displays that position.
 - Displays PGN comments.
 - Supports Recursive Annotated Variations (RAVS).
 - Will display one game or store many games in a convenient list for user
   selection.
 - Handles game fragments via the FEN tag.  This is very useful for
   tactics training, engame analysis, middlegame instruction, etc. See the
   puzzle.htm example.
 - if "puzzlemode" is "on" the applet will hide the answer (the scoresheet)
   until the user presses the ShowAnswer button or the ">" (next move) button.
   See puzzle.htm for an example.

 To use:

   Simply copy the contents of this zip file into a directory.
   There are three examples: Polgar-Anand.htm, hoogovens.htm, and puzzle.htm.
   View these files for a simple example on how to use the applet. Their
   repective pgn files are Polgar-Anand.pgn, a nicely annotated game by FIDE
   World Champion, Alexander Khalifman, hoogovens.zip (a zipped PGN game
   file) and QueenSacks.pgn.  You do not need to unzip hoogovens.zip (unless
   you want to look at the unzipped contents for yourself).

Requirements:

   The client browswer must support Java 1.1.   This includes the Internet
   Explorer 4.x and higher, and Netscape 4.06 and higher.  The HTML sample
   files include a Java Script that checks for this requirement and refers
   the user to UpgradeBrowser.htm (also included) if needed.

   Send any comments or questions to:

                             Michael@Keating.net

   You're welcome to visit my chess site that includes online chess playing,
   among other things, at:

                               www.MyChess.com

   Good luck!

   Michael Keating

   12/16/1999


Fixes - 08/01/04
 - The first game in the list now shows when clicking on it just as all the other games do.
 - When using the refresh option (for broadcasting tournaments), the background thread should
   now shut down properly when the browser is closed or the user leaves the applet's page.

Fixes - 01/02/06
 - The game list is now numbered
 - A rare condition where castling was considered legal is now fixed.  

Fixes - 01/16/06
 - When black has the first move in a FEN position, the moves now correctly start in the black
   column of the scoresheet.
 - Now handing move adornments such as "??", "!!", and "+??".
 - Incorporated the following fixes and enhancments send in from Gordon McKinney (thanks Gordon):
   Fixed: Deal with opening comments (crashed before) by placing the comment on the first move. 
   Enhancement: Deals with comment concatenation (opening RAV NAGs + comments work correctly) 
   Enhancement: Used the official PGN standard for NAG codes. 
   Enhancement: Added non standard (>139) NAG codes to support ChessBase / Fritz / HiArcs engine etc. 
   Enhancement: Modified NAG routine to support multiple NAGs with pretty hyphenation and spacing. 
   Enhancement: Modified NAG upper bound test to be variable using the list as the determinant. 
   Fixed: Compilation ambiguity with java.awt.List 


window.onload = function() {
    var toc = document.getElementById( "toc" );
    var tocCurrent = document.getElementById( "toc-current" );

    if( toc != null && tocCurrent != null ) {
        for( var current = tocCurrent.parentElement ; current != toc && current != null; current = current.parentElement ) {
            if( current.classList.contains( "toc" ) ) {
                current.classList.add( "toc-current-path" );
            }
        }
    }
}

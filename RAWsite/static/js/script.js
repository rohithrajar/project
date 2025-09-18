var audio = {
    init: function(){
    var $that=this;
        $(function(){
            $that.components.media();
        });
    },
    components:{
        media: function(target){
            var media=$('audio.fc-media',(target !== undefined)? target: 'body');
            if (media.length){
                media.mediaelementplayer({
                    audioHeight:40,
                features: ['playpause','current','duration','progress','volume','tracks','fullscreen'],
                    alwaysShowControls: true,
                    timeAndDurationsSeparator:'<span></span>',
                    iPaduseNativeControls: true,
                    iPhoneUseNativeControls: true,
                    AndroidUseNativeControls: true,

                });
            }
        },
    },
};

audio.init();

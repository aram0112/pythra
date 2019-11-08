from erlport.erlang import set_encoder, set_decoder

from pythra import decoders, encoders, logger, obj


def setup():
    logger.info("Setting up LFE Python ...")
    obj.init()
    setup_encoders()
    setup_decoders()


def setup_encoders():
    set_encoder(encoders.encode)


def setup_decoders():
    set_decoder(decoders.decode)

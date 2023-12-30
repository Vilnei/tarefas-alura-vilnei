import styled from "styled-components"


// essa parte com props e para poder escolher a cor que vc quiser as || server como OU
export const Titulo = styled.h2`
    width: 100%;
    padding: 30px 0;
    background-color: #FFF;
    color: ${props => props.cor || '#000'};
    font-size: ${props => props.tamanhoFonte || '36px'};
    text-align: ${props => props.alinhamento || 'center'};
    margin: 0;
`

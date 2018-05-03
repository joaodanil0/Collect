/**
 * Classe CustomGlobal - Representa todas as informacões que não pertencem a qualquer tipo de nó, mas sim ao ambiente
 * (dia, hora, minuto, segundo)
 * @author João Danilo &lt; joaodanilo1992@gmail.com&gt;
 * @version 1.0, 24/01/16
 */
package projects.Collect;

import sinalgo.configuration.Configuration;
import sinalgo.configuration.CorruptConfigurationEntryException;
import sinalgo.runtime.AbstractCustomGlobal;
import sinalgo.runtime.Global;


public class CustomGlobal extends AbstractCustomGlobal{
	
	/**Informa o segundo atual da simulação */	
	public static int segundo = 0;
	
	/**Informa o minuto atual da simulação */
	public static int minuto = 0;
	
	/**Informa a hora atual da simulação */
	public static int hora = 0;
	
	/**Informa a quantidade de dias atual da simulação */
	public static int num_dias = 0;	
	
	/**Informa o total de segundos por dia decorridos na simulação */
	public static double tempo = 1;	
	
	/**Informa se é dia ou noite na simulação */	
	public static boolean dia = false;	
	
	/**Informa a intensidade solar atual da simulacao */	
	public static float intensidadeSolar;
	
	/**Informa o multiplicador da intensidade solar */
	public static double multiplicadorIntensidade;
	
	public CustomGlobal(){
		
		try {
			multiplicadorIntensidade = Configuration.getDoubleParameter("radiationMultiplier/multiplier");
		} catch (CorruptConfigurationEntryException e) {
			e.printStackTrace();
		}
		
	}
	
	/**
	 * Verifica se é dia ou noite
	 * @return boolean dia
	 */
	protected boolean eDia(){
		
		if(hora >= 6 && hora < 18 ){
			
			return true;
		}
		else{
			
			return false;
		}		
	}
	
	/**
	 * Faz a contagem dos segundos da simulação
	 */	
	protected void contaSegundo(){
					
		segundo++;
				
		if(segundo == 60){
			
			segundo = 0;
		}		
		
	}
	
	/**
	 * Faz a contagem dos minutos da simulação
	 */	
	protected void contaMinuto(){
		
		if(Global.currentTime % 60 == 0){
			
			minuto++;
		}
		
		if(minuto == 60){
			
			minuto = 0;
		}
		
	}
	
	/**
	 * Faz a contagem das horas da simulação
	 */	
	protected void contaHora(){
		
		if(Global.currentTime % 3600 == 0){
			
			hora++;			
		}
		
		if(hora == 24){
			
			hora = 0;
		}
		
	}
	
	/**
	 * Faz a contagem dos dias da simulação
	 */	
	protected void contaDia(){
		
		if(Global.currentTime % 86400 == 0){
								
			num_dias++;
		}
	}
	
	/**
	 * Faz a contagem do total de segundos por dia da simulação
	 */	
	protected void contaSegundosPorDia(){		
		
		tempo++;		
		
		if(tempo % 86400 == 0){
			
			tempo = 0;
		}		
	}
	
	/**
	 * Calcula a intensidade solar a cada segundo do dia
	 * @return float intensidadeSolar
	 */
	public float getIntensidadeSolar(){
		
		float hora = (float) (tempo/3600);
		
		return (float) ((-27.778f * (Math.pow(hora, 2))) + (666.667f * hora) - 3000.024f)  ;
	}
	
	/**
	 * Primeiro método a ser chamado a cada round
	 */	
	public void preRun(){		
		
	}
	
	/**
	 * Último método a ser chamado a cada round
	 */	
	public void postRound(){
		
		dia = eDia();	
		
		intensidadeSolar = (getIntensidadeSolar() * ( (float) multiplicadorIntensidade));
		
		contaSegundo();
		
		contaMinuto();
		
		contaHora();
		
		contaDia();
		
		contaSegundosPorDia();
				
		
	}
	
	/**
	 * Verifica se a simulação acabou (Modo GUI)
	 * @return boolean hasTerminated
	 */	
	public boolean hasTerminated() {
		
		return false;
	} 
}

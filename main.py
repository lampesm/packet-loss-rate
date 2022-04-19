from typing import List
import time

from decouple import config
import pyshark


class Observer:
    def __init__(self, time_out, iface, ip_addr) -> None:
        self.__time_out: int = time_out
        self.__iface: str = iface
        self.__ip_addr: str = ip_addr
        self.__packet_loss: List = []
        self.__packet_success: List = []
        self.__tcp_dup_ack: List = []
        self.__tcp_per: List = []
        self.__tcp_ret: List = []
        self.__tcp_fast_ret: List = []
        self.__out_of_order: List = []
        self.__tcp_spu: List = []
    
    @property
    def runner(self) -> None:
        self.__packetـfinder
        self.__calculate_error_packets
        self.__print_calculations

    @property
    def __packetـfinder(self) -> None:
        self.capture = pyshark.LiveCapture(interface=self.__iface, only_summaries=True)
        print("starting !!!")
        start_time = time.time()

        for j, pkt in enumerate(self.capture):
            str_p = str(pkt)

            if self.__ip_addr in str_p:
                print(j, ": ", pkt)
                if (
                    "TCP Dup ACK" in str_p
                    or "TCP Previous" in str_p
                    or "TCP Retransmission" in str_p
                    or "TCP Fast Retransmission" in str_p
                    or "Out-Of-Order" in str_p
                    or "TCP Spurious Retransmission" in str_p
                ):
                    self.__packet_loss.append(str_p)
                else:
                    self.__packet_success.append(str_p)

            if time.time() - start_time > self.__time_out:
                capture.close()
                break
    
    @property
    def __calculate_error_packets(self) -> None:
        for pkt_loss in self.__packet_loss:
            if "TCP Dup ACK" in pkt_loss:
                self.__tcp_dup_ack.append(pkt_loss)
            elif "TCP Previous" in pkt_loss:
                self.__tcp_per.append(pkt_loss)
            elif "TCP Retransmission" in pkt_loss:
                self.__tcp_ret.append(pkt_loss)
            elif "TCP Fast Retransmission" in pkt_loss:
                self.__tcp_fast_ret.append(pkt_loss)
            elif "Out-Of-Order" in pkt_loss:
                self.__out_of_order.append(pkt_loss)
            elif "TCP Spurious Retransmission" in pkt_loss:
                self.__tcp_spu.append(pkt_loss)

    @property
    def __print_calculations(self) -> None:
        print("=" * 80)
        print(
            "Data transfer failure ratio = ",
            len(self.__packet_loss) / (len(self.__packet_loss) + len(self.__packet_success)) * 100,
            "%",
        )
        print(
            "Data transfer successful ratio = ",
            len(self.__packet_success) / (len(self.__packet_loss) + len(self.__packet_success)) * 100,
            "%",
        )
        print("=" * 80)
        print("TCP Dup ACK = ", len(self.__tcp_dup_ack) / len(self.__packet_loss) * 100, "%")
        print("TCP Previous = ", len(self.__tcp_per) / len(self.__packet_loss) * 100, "%")
        print("TCP Retransmission = ", len(self.__tcp_ret) / len(self.__packet_loss) * 100, "%")
        print("TCP Fast Retransmission = ", len(self.__tcp_fast_ret) / len(self.__packet_loss) * 100, "%")
        print("TCP Out-Of-Order = ", len(self.__out_of_order) / len(self.__packet_loss) * 100, "%")
        print("TCP Spurious Retransmission = ", len(self.__tcp_spu) / len(self.__packet_loss) * 100, "%")


if __name__ == "__main__":
    ob = Observer(config("LISTENING_TIME", cast=int), config("INTERFACE"), config("LISTENER"))
    ob.runner

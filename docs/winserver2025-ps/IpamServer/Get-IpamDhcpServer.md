---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDhcpServer.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdhcpserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDhcpServer
---

# Get-IpamDhcpServer

## 摘要
从IPAM数据库中获取有关DHCP服务器的信息。

## 语法

请帮我把这段Markdown格式的文本转换成中文。`
Get-IpamDhcpServer [[-ServerFqdn] <String[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
请帮我把这段Markdown格式的文本转换成中文。`

## 描述
`Get-IpamDhcpServer` cmdlet 可以获取有关 IP 地址管理（IPAM）服务器数据库中动态主机配置协议（DHCP）服务器的信息。DHCP 服务器负责将 IP 地址分配给客户端设备。

## 示例

### 示例 1：获取所有 DHCP 服务器的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDhcpServer
请帮我把这段Markdown格式的文本转换成中文。`

此命令会返回有关IPAM数据库中所有DHCP服务器的信息。

### 示例 2：获取关于单个 DHCP 服务器的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDhcpServer -ServerFqdn "dhcp.contoso.com"
请帮我把这段Markdown格式的文本转换成中文。`

此命令返回名为 dhcp.contoso.com 的单个 IPAM DHCP 服务器的相关信息。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -ServerFqdn
指定要返回的DHCP服务器的全限定域名（FQDN）。

`-ServerFqdn "dhcp.contoso.com"`

请帮我把这段Markdown格式的文本转换成中文。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -ThrottleLimit
指定可以同时运行的最大并发操作数量。如果省略此参数或输入值`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDhcpServer

此cmdlet返回一个对象，该对象表示**IpamDhcpServer**类的一个实例。

## 备注

## 相关链接

[Get-IpamDhcpScope](./Get-IpamDhcpScope.md)

[Get-IpamDhcpSuperscope](./Get-IpamDhcpSuperscope.md)

---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDhcpSuperscope.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdhcpsuperscope?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDhcpSuperscope
---

# Get-IpamDhcpSuperscope

## 摘要
从 IPAM 数据库中获取有关 DHCP 超范围（superscope）的信息。

## 语法

请帮我把这段Markdown格式的文本转换成中文。`
Get-IpamDhcpSuperscope [[-SuperscopeName] <String[]>] [[-ServerFqdn] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
请帮我把这段Markdown格式的文本转换成中文。`

## 描述
**Get-IpamDhcpSuperscope** cmdlet 可以从 IP 地址管理 (IPAM) 服务器数据库中获取有关动态主机配置协议 (DHCP) 超范围的信息。超范围表示 DHCP 服务器可以租给客户端的 IP 地址。在大多数情况下，超范围对应于 IP 子网。一般来说，DHCP 服务器只能从一个超范围中租用地址；但是，超范围提供了一种机制，使 DHCP 服务器能够从多个超范围中租用地址。需要注意的是，超范围仅适用于 IPv4 地址。

## 示例

#### 示例 1：获取所有超范围（superscopes）的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDhcpSuperscope
请帮我把这段Markdown格式的文本转换成中文。`

此命令会返回有关IPAM数据库中所有DHCP超级作用域的信息。

### 示例 2：获取服务器上所有超作用域（superscopes）的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDhcpSuperscope -ServerFqdn "dhcp.contoso.com"
请帮我把这段Markdown格式的文本转换成中文。`

此命令会返回在名为dhcp.contoso.com的DHCP服务器上找到的所有DHCP超范围（superscopes）。

### 示例 3：获取单个超范围（superscope）的信息
请帮我把这段Markdown格式的文本转换成中文。`
PS C:\> Get-IpamDhcpSuperscope -ServerFqdn "dhcp.contoso.com"-SuperscopeName "SuperScope01"
请帮我把这段Markdown格式的文本转换成中文。`

此命令返回名为 SuperScope01 的单个 DHCP 超范围的信息，该超范围位于名为 dhcp.contoso.com 的服务器上。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定用于获取 DHCP 超范围的 DHCP 服务器的完全限定域名。例如：

`-ServerFqdn "dhcp.contoso.com"`

请帮我把这段Markdown格式的文本转换成中文。

请帮我把这段Markdown格式的文本转换成中文。`yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
请帮我把这段Markdown格式的文本转换成中文。`

### -SuperscopeName
指定要检索的DNS超范围的名称。例如：.

`-SuperscopeName "太平洋西北地区"`

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的节流限制。这个节流限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Get-IpamDhcpSuperscope

此 cmdlet 返回一个对象，该对象代表 **Get-IpamDhcpSuperscope** 的一个实例。

## 备注

## 相关链接

[Get-IpamDhcpScope](./Get-IpamDhcpScope.md)

[Get-IpamDhcpServer](./Get-IpamDhcpServer.md)

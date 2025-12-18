---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerInDC_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/remove-dhcpserverindc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-DhcpServerInDC
---

# 从DC中删除DHCP服务器

## 摘要
从 Active Directory 中授权的 DHCP 服务器服务列表中删除指定的 DHCP 服务器服务。

## 语法

```
Remove-DhcpServerInDC [[-DnsName] <String>] [[-IPAddress] <IPAddress>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-DhcpServerInDC` cmdlet 会从 Active Directory 中授权的 DHCP 服务器服务列表中删除指定的动态主机配置协议（DHCP）服务器服务。

当您既不指定*DnsName*参数也不指定*IPAddress*参数时，本地DHCP服务器服务将从Active Directory中授权的DHCP服务器服务列表中删除。

如果您仅指定*DnsName*参数，那么在具有该DNS名称的计算机上运行的DHCP服务器服务将从AD中授权的DHCP服务器服务列表中删除。

如果您指定了*DnsName*和*IPAddress*参数，那么在具有这些指定值的计算机上运行的DHCP服务器服务将从Active Directory中授权的DHCP服务器服务列表中删除。

如果您只指定了 *IPAddress* 参数，系统会返回一个错误。

除了删除在域控制器（DC）中运行DHCP服务器服务的计算机之外，此cmdlet还会触发DHCP服务器服务执行授权检查。

即使尝试移除运行DHCP服务器服务的计算机时遇到“对象已存在”的错误，授权检查的触发仍然会执行。

如果运行 DHCP 服务器服务的计算机没有加入 Active Directory，并且服务器授权检查的触发条件得到了满足，则会显示以下警告：

DHCP服务器已经在Active Directory中被取消授权了。对DHCP服务器的授权检查已经启动。

如果运行DHCP服务器服务的计算机没有加入Active Directory（AD）域，且服务器授权检查的触发条件未能满足，系统将会显示以下警告：

DHCP服务器在Active Directory中的授权状态已被取消。尝试对DHCP服务器进行授权检查时失败了。错误代码：%d

如果成功删除了在 Active Directory 中运行 DHCP 服务器服务的计算机，但服务器授权检查的触发机制失败，则会显示以下警告：

DHCP服务器已在Active Directory中成功取消授权。尝试对DHCP服务器进行授权检查时失败。错误代码：%d

如果删除运行DHCP服务器服务并与Active Directory关联的计算机时出现除“object_does_notalreadyExists_error”之外的其他错误，系统会返回相应的错误信息，并且不会触发对该服务器的授权检查。

## 示例

### 示例 1：通过 DNS 名称和地址删除对象
```
PS C:\> Remove-DhcpServerInDC -DnsName "dhcpserver.contoso.com" -IPAddress 10.10.10.2
```

这个示例会删除 Active Directory 域中与该 DHCP 服务器服务相关联的对象。该 DHCP 服务器运行在名为 dhcpserver.contoso.com 的计算机上，其 IP 地址为 10.10.10.2。这样一来，该 DHCP 服务器服务将无法再为网络中的客户端提供服务（即该服务器将被“取消授权”）。

### 示例 2：通过 DNS 名称并查找 IP 地址来删除对象
```
PS C:\> Remove-DhcpServerInDC -DnsName "dhcpserver.contoso.com"
```

这个示例会删除 Active Directory 域中与 DHCP 服务器服务相关联的对象。该 DHCP 服务器服务运行在名为 dhcpserver.contoso.com 的计算机上，因此这一操作会导致该 DHCP 服务器服务无法再为网络中的客户端提供服务。要获取运行 DHCP 服务器服务的计算机的 IP 地址，可以在 DNS 中查询 dhcpserver.contoso.com。

### 示例 3：删除本地计算机上的一个对象
```
PS C:\> Remove-DhcpServerInDC
```

这个示例用于删除 Active Directory 域中与本地计算机上运行的 DHCP 服务器服务相关联的对象。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您确认是否要执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DnsName
指定运行DHCP服务器服务的计算机的DNS名称，以便对该计算机进行授权撤销（即取消其作为DHCP服务器的资格）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPAddress
指定运行DHCP服务器服务的计算机的IP地址，以便取消对该计算机的授权（即停止该计算机使用DHCP服务）。

```yaml
Type: IPAddress
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略了此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算出一个最优的并发限制。这个并发限制仅适用于当前的命令，而不适用于整个会话或整个计算机。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerInDC
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerInDC
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerInDC](./Add-DhcpServerInDC.md)

[Get-DhcpServerInDC](./Get-DhcpServerInDC.md)


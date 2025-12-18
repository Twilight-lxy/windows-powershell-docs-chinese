---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerInDC_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/add-dhcpserverindc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-DhcpServerInDC
---

# 使用 Add-DhcpServerInDC 命令将 DHCP 服务器添加到域控制器 (Domain Controller) 中

## 摘要
将运行DHCP服务器服务的计算机添加到Active Directory中授权的DHCP服务器服务列表中。

## 语法

```
Add-DhcpServerInDC [[-DnsName] <String>] [[-IPAddress] <IPAddress>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-DhcpServerInDC` cmdlet 将运行 DHCP 服务器服务的计算机添加到 Active Directory 中授权的动态主机配置协议（DHCP）服务器服务列表中。在已加入域的计算机上运行的 DHCP 服务器服务必须在 Active Directory 中获得授权，才能在网络中开始分配 IP 地址。

如果你既没有指定 *DnsName* 参数，也没有指定 *IPAddress* 参数，那么本地服务器将会被添加到 Active Directory 中。

如果您只指定*DnsName*参数，则指定的域名系统（DNS）名称会被添加到Active Directory中。

在这两种情况下，任何被添加到域控制器中的、用于运行DHCP服务器服务的计算机的IP地址都会作为Active Directory中服务器对象的一部分被记录下来。

如果您指定了*DnsName*和*IPAddress*参数，该对象将被添加到具有指定值的域控制器中。

除了在数据中心（DC）中添加运行DHCP服务器服务的计算机之外，这个cmdlet还会触发DHCP服务器服务执行授权检查。

即使尝试添加用于运行DHCP服务器服务的计算机时出现“对象已存在”的错误，授权检查的触发过程仍然会执行。

如果运行 DHCP 服务器服务的计算机已经获得了授权，并且服务器授权检查的触发条件也满足成功，那么将会显示以下警告信息：

DHCP服务器已经在Active Directory中获得了授权。对DHCP服务器的授权检查已经启动。

如果运行DHCP服务器服务的计算机已经获得了授权，但服务器授权检查的触发条件未能满足，则会显示以下警告：

DHCP服务器已经在Active Directory中获得了授权。尝试对DHCP服务器进行授权检查时失败了。错误代码：%d

如果成功将运行 DHCP 服务器服务的计算机添加到 Active Directory 中，但服务器授权检查的触发器失败，则会显示以下警告：

DHCP服务器已成功在Active Directory中授权。但尝试对DHCP服务器进行授权检查时失败了。错误代码：%d

如果尝试将运行 DHCP 服务器服务的计算机添加到 Active Directory 时出现除 “object_ALREADYexists_error” 以外的其他错误，系统会返回相应的错误信息，并且不会触发对服务器的授权检查。

## 示例

### 示例 1：为 DHCP 服务器服务添加一个对象
```
PS C:\> Add-DhcpServerInDC -DnsName "dhcpserver.contoso.com" -IPAddress 10.10.10.2
```

这个示例在 Active Directory 域中为 DHCP 服务器服务添加了一个对象。该 DHCP 服务器运行在一台计算机上，这台计算机的 DNS 名称为 dhcpserver.contoso.com，IP 地址为 10.10.10.2，并授权该 DHCP 服务器服务为网络中的 DHCP 客户端提供服务。

### 示例 2：为 DHCP 服务器服务添加一个用于查询 IP 地址的对象
```
PS C:\> Add-DhcpServerInDC -DnsName "dhcpserver.contoso.com"
```

这个示例在 Active Directory 域中为运行在名为 dhcpserver.contoso.com 的计算机上的 DHCP 服务器服务添加了一个对象，并授权该 DHCP 服务器服务为网络中的 DHCP 客户端提供服务。Active Directory 中的 DHCP 服务器服务对象的 IP 地址是通过在 DNS 中查找 dhcpserver.contoso.com 获得的。

### 示例 1：在本地计算机上为 DHCP 服务器服务添加一个对象，并实现基于 IP 地址的查找功能
```
PS C:\> Add-DhcpServerInDC
```

这个示例在 Active Directory 域中为本地计算机上运行的 DHCP 服务器服务添加了一个对象。通过喺 DNS 中查找本地计算机的主机名，可以获取该计算机在 Active Directory 中的 IP 地址。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 获得的会话对象）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
在运行该cmdlet之前，会提示您进行确认。

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
指定运行 DHCP 服务器服务的计算机的 DNS 名称，以便将其添加到 Active Directory 中授权的 DHCP 服务器服务列表中。

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
指定运行 DHCP 服务器服务的计算机的 IP 地址，该计算机将被添加到 Active Directory 中授权的 DHCP 服务器服务列表中。

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
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算出一个最优的并发限制。该并发限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet运行会发生的情景。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerInDC
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows Management Instrumentation（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerInDC
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于展示 Windows Management Instrumentation（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Get-DhcpServerInDC](./Get-DhcpServerInDC.md)

[Remove-DhcpServerInDC](./Remove-DhcpServerInDC.md)


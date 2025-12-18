---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerInDC_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverindc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerInDC
---

# Get-DhcpServerInDC

## 摘要
从 Active Directory 中检索运行 DHCP 服务器服务的授权计算机的列表。

## 语法

```
Get-DhcpServerInDC [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerInDC` cmdlet 从 Active Directory 中检索运行动态主机配置协议（DHCP）服务器服务的授权计算机的列表。只有那些在 Active Directory 中被授权的、且实际正在运行 DHCP 服务器服务的计算机，才能在网络中租用 IP 地址。

## 示例

### 示例 1：获取域中所有运行 DHCP 协议的计算机
```
PS C:\> Get-DhcpServerInDC
```

这个示例获取了所有在Active Directory域中授权且运行DHCP服务器服务的计算机的列表。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 将根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerInDC[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Add-DhcpServerInDC](./Add-DhcpServerInDC.md)

[Remove-DhcpServerInDC](./Remove-DhcpServerInDC.md)


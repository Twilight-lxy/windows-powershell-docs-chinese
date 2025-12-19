---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCapabilities.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamcapability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamCapability
---

# Get-IpamCapability

## 摘要
获取 IPAM 中的所有可选功能。

## 语法

```
Get-IpamCapability [-Capability <Capability[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-IpamCapability` cmdlet 可获取互联网协议地址管理（IPAM）中所有可用的可选功能。如果您不指定 `Capability` 参数，该 cmdlet 会获取 IPAM 中的所有可选功能。默认情况下，IPAM 会启用所有可用的可选功能。

使用 **Disable-IpamCapability** cmdlet 来禁用某个可选的 IPAM 功能；使用 **Enable-IpamCapability** cmdlet 来启用某个可选的 IPAM 功能。

目前，IP地址追踪是唯一可用的可选功能。

## 示例

#### 示例 1：获取 IPAM 中的所有可选功能
```
PS C:\> Get-IpamCapability
Name                                                        Status

----                                                        ------

IpAddressTracking                                           Enabled
```

这个命令可以获取 IPAM 中所有可用的可选功能以及这些功能的当前状态。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -Capability
指定一个可选的IPAM功能数组。目前，IpAddressTracking是该参数的唯一有效值。

```yaml
Type: Capability[]
Parameter Sets: (All)
Aliases:
Accepted values: IpAddressTracking

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，也可以输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamCapability
一个对象，用于表示可选的 IPAM（IP 地址管理）功能及其状态（启用/禁用）。

## 备注

## 相关链接

[Enable-Ipam Capability](./Enable-IpamCapability.md)

[ Disable-Ipam Capability](./Disable-IpamCapability.md)


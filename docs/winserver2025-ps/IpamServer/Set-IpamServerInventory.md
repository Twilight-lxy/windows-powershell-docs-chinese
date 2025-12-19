---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamServerInventory.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamserverinventory?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamServerInventory
---

# 设置 IpamServerInventory

## 摘要
修改 IPAM 服务器清单中基础设施服务器的属性。

## 语法

```
Set-IpamServerInventory [-Name] <String> [[-NewName] <String>] [-ManageabilityStatus <ManageabilityStatus>]
 [-Owner <String>] [-ServerType <ServerRole[]>] [-Description <String>] [-AddCustomConfiguration <String>]
 [-RemoveCustomConfiguration <String>] [-Force] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamServerInventory` cmdlet 用于修改 IP 地址管理（IPAM）服务器库存中某个基础设施服务器的属性。可以使用服务器名称或完全限定域名（FQDN）来标识该服务器。如果仅指定服务器名称，IPAM 会尝试解析该服务器名称。

## 示例

### 示例 1：修改服务器的属性
```
PS C:\> Set-IpamServerInventory -Name "Dhcp01" -ManageabilityStatus Managed -PassThru
```

该命令修改了名为Dhcp01的基础设施服务器的属性，使其能够通过IPAM进行管理。

该命令包含了*PassThru*参数，因此它会将结果显示在控制台上。

## 参数

### -AddCustomConfiguration
指定要添加到服务器清单中的自定义配置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -Description
为服务器指定一个描述。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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

### -ManageabilityStatus
指定服务器的可管理性状态。

该参数的可接受值为：

- Unspecified
- Managed
- Unmanaged

If you specify a value of Managed for this parameter, IPAM gathers data from the server.

```yaml
Type: ManageabilityStatus
Parameter Sets: (All)
Aliases:
Accepted values: Unspecified, Unmanaged, Managed

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定要修改的基础设施服务器的完全限定域名（FQDN）。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ServerName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NewName
用于指定基础设施服务器的新名称或完全 Qualified Domain Name（FQDN）。IPAM 会尝试将名称解析为 IP 地址；如果无法完成解析，则会报告错误。

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

### -Owner
指定动态主机配置协议（DHCP）服务器的所有者。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -RemoveCustomConfiguration
指定需要修改的元数据字段。将元数据以一系列自定义字段名称的形式列出，并用分号（;）分隔。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServerType
指定服务器上存在的服务器角色数组。

该参数的可接受值为：

- DHCP
- DC
- DNS
- NPS

```yaml
Type: ServerRole[]
Parameter Sets: (All)
Aliases:
Accepted values: DC, DNS, DHCP, NPS

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamServerInventory
此cmdlet返回一个对象，该对象代表IPAM系统中的基础设施服务器。

## 备注

## 相关链接

[Add-IpamServerInventory](./Add-IpamServerInventory.md)

[Get-IpamServerInventory](./Get-IpamServerInventory.md)

[Remove-IpamServerInventory](./Remove-IpamServerInventory.md)


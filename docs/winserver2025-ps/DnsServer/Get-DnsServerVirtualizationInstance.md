---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerVirtualizationInstance_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsservervirtualizationinstance?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerVirtualizationInstance
---

# Get-DnsServerVirtualizationInstance

## 摘要
获取DNS服务器上的虚拟化实例。

## 语法

```
Get-DnsServerVirtualizationInstance [-ComputerName <String>] [[-Name] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerVirtualizationInstance` cmdlet 用于获取域名系统（DNS）服务器上的虚拟化实例。如果提供了 `Name` 参数，该 cmdlet 将返回相应的虚拟化实例。

## 示例

#### 示例 1：显示关于虚拟化实例的信息
```
PS C:\> Get-DnsServerVirtualizationInstance -Name 8231 | fl *
Description            : This virtualization instance hosts the zones for the Host tenant
FriendlyName           : HostTenantPartition
VirtualizationInstance : 8231
PSComputerName         :
CimClass               : root/Microsoft/Windows/DNS:DnsServerVirtualizationInstance
CimInstanceProperties  : {Description, FriendlyName, VirtualizationInstance}
CimSystemProperties    : Microsoft.Management.Infrastructure.CimSystemProperties
```

这个命令会显示关于名为“8231”的虚拟化实例的信息。

### 示例 2：显示 DNS 服务器上的所有虚拟化实例
```
PS C:\> Get-DnsServerVirtualizationInstance | fl *
Description            :
FriendlyName           : Default
VirtualizationInstance : .
PSComputerName         :
CimClass               : root/Microsoft/Windows/DNS:DnsServerVirtualizationInstance
CimInstanceProperties  : {Description, FriendlyName, VirtualizationInstance}
CimSystemProperties    : Microsoft.Management.Infrastructure.CimSystemProperties

Description            : This virtualization instance hosts the zones for the 'Host' tenant
FriendlyName           : RedTenantPartition
VirtualizationInstance : 8231
PSComputerName         :
CimClass               : root/Microsoft/Windows/DNS:DnsServerVirtualizationInstance
CimInstanceProperties  : {Description, FriendlyName, VirtualizationInstance}
CimSystemProperties    : Microsoft.Management.Infrastructure.CimSystemProperties
Description            : This virtualization instance hosts the zones for tenant blue
FriendlyName           : TenantBluePartition
VirtualizationInstance : 9743
PSComputerName         :
CimClass               : root/Microsoft/Windows/DNS:DnsServerVirtualizationInstance
CimInstanceProperties  : {Description, FriendlyName, VirtualizationInstance}
CimSystemProperties    : Microsoft.Management.Infrastructure.CimSystemProperties
```

这个命令显示了DNS服务器上的虚拟化实例，包括由句点（.）表示的默认虚拟化实例。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ComputerName
指定此cmdlet执行命令的远程计算机。请输入该远程计算机的NetBIOS名称或完全限定的域名。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
以字符串数组的形式指定虚拟化实例的唯一标识符。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: VirtualizationInstance

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前运行的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerVirtualizationInstance[]

## 备注

## 相关链接

[Add-DnsServerVirtualizationInstance](./Add-DnsServerVirtualizationInstance.md)

[Remove-DnsServerVirtualizationInstance](./Remove-DnsServerVirtualizationInstance.md)

[Set-DnsServerVirtualizationInstance](./Set-DnsServerVirtualizationInstance.md)


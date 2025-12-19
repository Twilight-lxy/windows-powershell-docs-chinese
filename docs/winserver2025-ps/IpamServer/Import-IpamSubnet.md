---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamSubnet.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/import-ipamsubnet?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-IpamSubnet
---

# 导入 Ipam 子网

## 摘要
从指定的文件中导入IP地址子网对象到IPAM系统中。

## 语法

```
Import-IpamSubnet -Path <String> -AddressFamily <AddressFamily> [-ErrorPath <String>] [-Force]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-IpamSubnet` 这个 cmdlet 会将指定文件中的 IP 地址子网对象导入到运行 IP 地址管理（IPAM）服务器的计算机中。在导入过程中，如果遇到无法导入的对象，该 cmdlet 会记录相应的错误信息。您可以使用这个 cmdlet 导入无论是虚拟化还是非虚拟化的子网。该 cmdlet 会将 .csv 文件中的数据（以逗号分隔的形式）添加到运行 IPAM 服务器的计算机中，并使用 .csv 文件中指定的更新信息来修改现有的子网对象。.csv 文件可以同时包含虚拟化和非虚拟化的子网信息。

如果导入的文件头部没有 `NetworkType`、`ProviderAddressSpace` 和 `CustomerAddressSpace` 这些列，那么 cmdlet 会假设所有子网都是非虚拟化的，并将它们添加到默认地址空间中。如果文件头部包含这些列，则 cmdlet 会根据网络类型将这些子网分别添加到相应的提供者或客户地址空间中。

## 示例

### 示例 1：导入 IPv4 子网
```
PS C:\> Import-IpamSubnet -AddressFamily IPv4 -Path "C:\subnetsv4.csv" -Force
```

该命令将文件 `Subnetsv4.csv` 中的 IPv4 子网导入到运行 IPAM 的计算机中。该命令会添加新的子网并修改现有的地址信息，同时会将任何出现的错误记录在用户所在系统的默认文件夹 `%windir%\temp` 下，以 `.csv` 文件格式保存。

### 示例 2：导入 IPv4 子网并指定错误处理路径
```
PS C:\> Import-IpamAddress -AddressFamily IPv4 -Path "C:\addressv4.csv" -ErrorPath "C:\" -Force
```

该命令从文件 Subnetsv4.csv 中导入 IPv4 子网到运行 IPAM 服务器的计算机上。该命令会添加新的子网，并修改现有的子网。

## 参数

### -AddressFamily
指定要导入的 IP 地址范围对象的地址族。该参数的可接受值为：

- IPv4
- IPv6

You can specify only one address family at a time using this cmdlet and the records in the file should match the address family you specify with this parameter.

```yaml
Type: AddressFamily
Parameter Sets: (All)
Aliases:
Accepted values: IPv4, IPv6

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -ErrorPath
该参数指定了当一个或多个记录导入失败时所生成的错误文件的全路径（包括目录和文件名），但不包括文件的实际名称。IPAM服务器会在文件名前添加 “Error_” 字符串，并在文件名后附加操作的时间戳来生成文件名。此参数的默认值为 `%windir%\temp` 文件夹。

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

### -Path
指定要导入的文件的完全限定路径和名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最优限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果该cmdlet被运行会发生的结果。但实际上该cmdlet并没有被运行。

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

## 输出

## 备注

## 相关链接

[Add-IpamSubnet](./Add-IpamSubnet.md)

[Export-IpamSubnet](./Export-IpamSubnet.md)

[Get-IpamSubnet](./Get-IpamSubnet.md)

[Remove-IpamSubnet](./Remove-IpamSubnet.md)

[Set-IpamSubnet](./Set-IpamSubnet.md)

